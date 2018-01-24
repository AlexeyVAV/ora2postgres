import cx_Oracle
import psycopg2
import time

###### Oracle part
def ora_conn(): # Oracle connection
    print("Oracle connection")
    tstart = time.time()
    ora_conn = cx_Oracle.connect("system", "RosE#3358", "exa_uscomdev1")
    tend = time.time()
    print("connected in {} sec".format(tend-tstart))

    return ora_conn
    #for ins_sql in do_ora_query(ora_conn):
    #    print(ins_sql)
    #ora_conn.close()

def ora_conn_close(ora_conn):
    ora_conn.close()

def do_ora_query(conn): # main oracle loop through all schema tables
    cursor = conn.cursor()
    cursor.execute("""SELECT table_name 
                        FROM dba_tables 
                        WHERE owner = :iowner
                        and rownum < 2""",
                        #and table_name = :itable""",
                    iowner = 'MARKETPLACE')
                    #,itable = 'META_DICTIONARY')

    #ins_list = [] # list of inserts
    ins_dict = {}
    for tname in cursor:
        print("Table_name:", tname[0])
        insert_statement = 'INSERT INTO {}.{} ('.format('MARKETPLACE',tname[0])
        values_str = '' # string to add bind variavle into VALUES clause of INSERT
        cnt = 1

        for cols in tab_col(conn, tname[0]):
            insert_statement += str(cols) + ', '
            #values_str = values_str + ':{}, '.format(cnt)
            values_str = values_str + '%s, '.format(cnt)
            cnt += 1

        #print('{}) VALUES({})'.format(insert_statement[:-2], values_str[:-2]))
        insert_statement = '{}) VALUES({})'.format(insert_statement[:-2], values_str[:-2]) # building INSERT string
        ins_dict[tname[0]] = insert_statement
        #ins_list.append(insert_statement)

    cursor.close()
    #print(ins_dict)
    return ins_dict

def tab_col(iconn, itable): # scan table for columns name
    cur = iconn.cursor() # table columns cursor

    cur.execute("""SELECT column_name 
                        FROM dba_tab_cols 
                        WHERE table_name = :i_table
                        and owner = :i_owner and column_id is not null order by column_id""",
                i_owner = 'MARKETPLACE',
                i_table=itable)

    #print("Columns for {}:".format(itable))
    col_list = [] # list of columns
    for colname in cur:
        col_list.append(colname[0])
    #    print(colname[0])
    #print(col_list)
    cur.close()
    return col_list

def ora_get_data(oraconn, itable):
    cur = oraconn.cursor()
    isql = "SELECT * FROM {}.{}".format('MARKETPLACE',itable)
    cur.execute (isql)
    data = list(cur)
    cur.close()
    return data

###### Postgres part
def do_pstg_query( conn ) :
    cur = conn.cursor()
    cur.execute( "SELECT * FROM vav_test" )
    for firstname, lastname in cur.fetchall() :
        print firstname, lastname
    cur.close()


def do_pstg_insert(pconn, iinsert, idata):
    print("Insert records into Postgres")
    try:
        ins_cur = pconn.cursor()
        #ins_cur.execute("prepare ora_ins as"
        #                "SELECT * FROM $1")
        #ins_cur.executemany(sql)
        #sql = ""
        ins_cur.executemany(iinsert, idata)
        #for firstname, lastname in ins_cur.fetchall() :
        #    print firstname, lastname
        ins_cur.commit()
    except (Exception, pconn.DatabaseError) as error:
        print(error)

    ins_cur.close()

def pstg_conn():
    print('Postgres connection')
    tstart = time.time()
    pstg_connection = psycopg2.connect("host='us-ham-svb-2051' port='5459' user='alexeyv' password='iamgroot' dbname='uscomdv1'")
    tend = time.time()
    print("connected in {} sec".format(tend - tstart))
    # port = 5459
    #do_pstg_query( pstg_connection )
    #do_pstg_insert(pstg_connection, 'vav_test')
    #pstg_connection.close()
    return pstg_connection

def pstg_conn_close(ptgconn):
    ptgconn.close()

###### MAIN part ######
def main():
    ioraconn = ora_conn()
    ipstgconn = pstg_conn()

    for ins_table, ins_sql in do_ora_query(ioraconn).iteritems():
        print("table to insert: {}  Insert Statement: {}".format(ins_table, ins_sql))
        print("Insert records into Postgres")
        ora_data = ora_get_data(ioraconn, ins_table)

        print(ora_data)
        for idata in ora_get_data(ioraconn, ins_table):
            try:
                ins_cur = ipstgconn.cursor()
                print([idata])
                ins_cur.execute(ins_sql, [idata])
                ins_cur.commit()
            except (Exception, ipstgconn.DatabaseError) as error:
                print(error)
            ins_cur.close()

        #for idata in ora_get_data(ioraconn, ins_table):
        #    do_pstg_insert(ipstgconn, ins_sql, idata)
        #    print(idata)


    #do_pstg_query(ipstgconn)
    #do_pstg_insert(ipstgconn,1)

    #pstg_conn_close(ipstgconn)
    ora_conn_close(ioraconn)


#
if __name__ == '__main__':
    main()