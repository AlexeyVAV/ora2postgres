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

    for ins_sql in do_query_ora(ora_conn):
        print(ins_sql)

    ora_conn.close()

def do_query_ora(conn): # mail oracle loop through all schema tables
    cursor = conn.cursor()
    cursor.execute("""SELECT table_name 
                        FROM dba_tables 
                        WHERE owner = :iowner
                        and rownum < 3""",
                        #and table_name = :itable""",
                    iowner = 'MARKETPLACE')
                    #,itable = 'META_DICTIONARY')

    ins_list = [] # list of inserts
    for tname in cursor:
        print("Table_name:", tname[0])
        insert_statement = 'INSERT INTO {}.{} ('.format('MARKETPLACE',tname[0])
        values_str = '' # string to add bind variavle into VALUES clause of INSERT
        cnt = 1

        for cols in tab_col(conn, tname[0]):
            insert_statement += str(cols) + ', '
            values_str = values_str + ':{}, '.format(cnt)
            cnt += cnt

        #print('{}) VALUES({})'.format(insert_statement[:-2], values_str[:-2]))
        insert_statement = '{}) VALUES({});'.format(insert_statement[:-2], values_str[:-2]) # building INSERT string
        ins_list.append(insert_statement)

    cursor.close()
    return ins_list

def tab_col(iconn, itable): # scan table for columns name
    cur = iconn.cursor() # table columns cursor
    cur.execute("""SELECT column_name 
                        FROM dba_tab_cols 
                        WHERE table_name = :i_table
                        and owner = :i_owner and column_id is not null""",
                i_owner = 'MARKETPLACE',
                i_table=itable)
                #i_table = 'META_DICTIONARY')
    print("Columns for {}:".format(itable))
    col_list = [] # list of columns
    for colname in cur:
        col_list.append(colname[0])
    #    print(colname[0])
    #print(col_list)
    cur.close()
    return col_list

###### Postgres part
def do_query_psg( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT * FROM vav_test" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname

def pstg_conn():
    print('Postgres connection')
    myConnection = psycopg2.connect("host='us-ham-svb-2051' port='5459' user='alexeyv' password='iamgroot' dbname='uscomdv1'")
    # port = 5459
    do_query_psg( myConnection )
    myConnection.close()

###### MAIN part ######
def main():
    ora_conn()
    #pstg_conn()

#
if __name__ == '__main__':
    main()