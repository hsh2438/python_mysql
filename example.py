class DBconfig:
    host = '127.0.0.1'
    port = 3306
    user = root
    passwd = admin123
    db = 'db_name'
    charset = 'utf8'

def __start_connection():
    conn = pymysql.connect(host=DBconfig.host, port=DBconfig.port, user=DBconfig.user, passwd=DBconfig.passwd, db=DBconfig.db_name, charset=DBconfig.charset)
    cursor = conn.cursor()
    return conn, cursor


def __stop_connection(conn):
    if conn.open:
        conn.close()
