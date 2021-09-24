from config import Config
import psycopg2

class Database:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def connect(self):
        conf = Config()
        self.conn = psycopg2.connect(
            dbname=conf.db_name,
            user=conf.db_user,
            password=conf.db_pass,
            host=conf.db_host,
            port=conf.db_port
        )

    def get_cursor(self):
        self.cursor = self.conn.cursor()

    def query(self, query):
        if self.conn is None:
            self.connect()
        if self.cursor is None:
            self.get_cursor()
        res = self.__execute(query)
        print(res)
        return res

    def __execute(self, query):
        self.cursor.execute(query)
        self.conn.commit()
        return self.cursor.fetchone()
