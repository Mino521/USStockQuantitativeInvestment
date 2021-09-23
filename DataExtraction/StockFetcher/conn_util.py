import mysql.connector

PORT = "3306"
DATABASE = "stockDB"
SERVER_NO = 1
SERVER = {"host": ["localhost", "cadb.cc0uav02d2tx.ap-southeast-2.rds.amazonaws.com"],
          "user": ["root", "admin"],
          "password": ["111111", "HtIONyOLbioppFsbdSsG"]}


def my_connector(host=SERVER["host"][SERVER_NO],
                 user=SERVER["user"][SERVER_NO],
                 password=SERVER["password"][SERVER_NO],
                 connect_database=True):
    if connect_database:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            port=PORT,
            database=DATABASE
        )
    else:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=password,
            port=PORT
        )
    return conn
