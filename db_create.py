import psycopg2

def database_create(setup_sql, db_name):
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1")
    cr = conn.cursor()

    try:
        cr.execute(setup_sql)
        cr.execute('SELECT create_db(%s)', (db_name,))
    finally:
        cr.close()
    conn.commit()

def tables_create(setup_sql):
    conn = psycopg2.connect(dbname="musicdb", user="postgres", password="1234", host="127.0.0.1")
    cr = conn.cursor()

    try:
        cr.execute(setup_sql)
        cr.execute('SELECT create_tables()')
    finally:
        cr.close()
    conn.commit()

def drop_tables(setup_sql):
    conn = psycopg2.connect(dbname="musicdb", user="postgres", password="1234", host="127.0.0.1")
    cr = conn.cursor()

    try:
        cr.execute(setup_sql)
        cr.execute('SELECT drop_database(%s)', (db_name,))
    finally:
        cr.close()
    conn.commit()