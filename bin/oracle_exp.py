import cx_Oracle
import psycopg2


def ora_conn():
    print("Oracle connection")
    ora_conn = cx_Oracle.connect("system", "", "exa_uscomdev1")
    do_query_ora(ora_conn)
    ora_conn.close()

def do_query_ora(conn):
    cursor = conn.cursor()
    cursor.execute("""SELECT table_name 
                        FROM dba_tables 
                        WHERE owner = :iowner
                        and table_name = :itable""",
                    iowner = 'MARKETPLACE',
                    itable = 'META_DICTIONARY')
    for tname in cursor:
        print("Table_names:", tname)
        tab_col(conn, tname)

def tab_col(iconn, itable):
    cur = iconn.cursor()
    cur.execute("""select column_name 
                        from dba_tab_cols 
                        where table_name = :i_table
                        and owner = :i_owner
                        and column_id is not null""",
                    i_table = itable,
                    i_owner = 'MARKETPLACE')
    for colname in cur:
        print(colname)

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

############
def main():
    ora_conn()
    #pstg_conn()

#
if __name__ == '__main__':
    main()