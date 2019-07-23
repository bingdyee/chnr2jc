# -*- coding: utf-8 -*-
import pymysql
import functools
from .utils import Singleton
from .models import Model
from settings import (DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD, DB_CHARSET)


@Singleton
class JdbcTemplate:

    def __init__(self, user='root', password='root', database='code_generator', host='127.0.0.1', port=3306,
                 charset='utf8mb4'):
        self.conn = pymysql.connect(
            host=host,
            user=user,
            port=port,
            password=password,
            database=database,
            charset=charset,
            connect_timeout=30
        )

    def __del__(self):
        self.conn.close()

    def select(self, sql, params=None):
        """
        Select
        Return: dict
        """
        with self.conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
            cursor.execute(sql, params)
            results = cursor.fetchall()
            return [row for row in results]

    def execute(self, sql, params=None):
        """
        For Delete Update Insert
        """
        with self.conn.cursor() as cursor:
            state = cursor.execute(sql, params)
        self.conn.commit()
        return state > 0

    def close(self):
        self.conn.close()


def init():
    return JdbcTemplate(host=DB_HOST, port=DB_PORT, user=DB_USER, password=DB_PASSWORD, database=DB_NAME,
                        charset=DB_CHARSET)


def mapper(func):
    """@mapper
    sql template & column to object
    """

    @functools.wraps(func)
    def inner(*args, **kwargs):
        sql = func(*args, **kwargs)
        jdbc = JdbcTemplate()
        annotations = func.__annotations__
        r_type = annotations.get('return')
        records = jdbc.select(sql, *args, **kwargs)
        if not len(records):
            return records
        if r_type.__module__ == 'typing':
            if r_type.__args__ and \
                    issubclass(r_type.__args__[0], Model):
                return [r_type.__args__[0](**record) for record in records]
        if issubclass(r_type, Model):
            return r_type(**records[0])
        return jdbc.execute(sql, *args, **kwargs)

    return inner


init()
