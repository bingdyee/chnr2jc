# -*- coding: utf-8 -*-
import pymysql


class JdbcTemplate:

    def __init__(self, user, password, database, host='127.0.0.1', charset='utf8mb4'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset=charset
        )

    def __del__(self):
        self.conn.close()

    def select(self, sql, params=None):
        with self.conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, params)
            results = cursor.fetchall()
            return [row for row in results]

    def update(self, sql, params=None):
        pass

    def delete(self, sql, params=None):
        pass
    
    def insert(self, sql, params=None):
        pass

    def close(self):
        self.conn.close()