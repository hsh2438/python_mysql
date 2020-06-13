import pymysql


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

        
# for select -> fetchall(), fetchone(), fetchmany(size)
# for insert, update, delete -> commit()

"""
import pymysql

db = pymysql.connect(host='funcoding-db.ca1fydhpobsc.ap-northeast-2.rds.amazonaws.com', port=3306, user='davelee', passwd='korea123', db='dave_db', charset='utf8')
try:
    with db.cursor() as cursor:
        sql = '
            CREATE TABLE korea (
                   id INT UNSIGNED NOT NULL AUTO_INCREMENT,
                   name VARCHAR(20) NOT NULL,
                   model_num VARCHAR(10) NOT NULL,
                   model_type VARCHAR(10) NOT NULL,
                   PRIMARY KEY(id)
            );
        '
        cursor.execute(sql)
        db.commit()
finally:
    db.close()
"""
