import cx_Oracle
import psycopg2

def ora_conn():
    conn = cx_Oracle.connect("system", "", "dhemrep_uksrv")
    cursor = conn.cursor()
    cursor.execute("""SELECT table_name 
                        FROM dba_tables 
                        WHERE owner = :iowner""",
                    iowner = 'XDB')
    for tname in cursor:
        print("Table_names:", tname)

def do_query( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT * FROM vav_test" )

    for firstname, lastname in cur.fetchall() :
        print firstname, lastname

def pstg_conn():
    print('Postgres connection')
    myConnection = psycopg2.connect("host='us-ham-svb-2051' port='5459' user='alexeyv' password='iamgroot' dbname='uscomdv1'")
    # port = 5459
    do_query( myConnection )
    myConnection.close()

############
def main():
    ora_conn()
    #pstg_conn()

#
if __name__ == '__main__':
    main()