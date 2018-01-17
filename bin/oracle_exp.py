import cx_Oracle

conn = cx_Oracle.connect("system", "welcome", "localhost/orclpdb")

    cursor = conn.cursor()
    cursor.execute("""
            SELECT table_name
            FROM dba_tables
            WHERE owner :iowner""",
            iowner = 'MARKETPLACE')
    for tname in cursor:
        print("Table_names:", tname)