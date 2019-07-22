# -*- coding: utf-8 -*-
import json
from datetime import datetime


class Model:

    def __call__(self):
        return self.json()

    def json(self):
        rs = self.__dict__
        for k, v in rs.items():
            rs[k] = v.strftime('%Y-%m-%d %H:%M:%S') if isinstance(v, datetime) else v
        return rs


class Column(Model):

    def __init__(self, table_name=None,
                 column_name=None,
                 data_type=None,
                 column_comment=None,
                 nullable=None,
                 column_key=None,
                 extra=None,
                 privileges=None):
        self.table_name = table_name
        self.column_name = column_name
        self.data_type = data_type
        self.column_comment = column_comment
        self.nullable = nullable
        self.column_key = column_key
        self.extra = extra
        self.privileges = privileges
        self.var_name = None
        self.method_name = None
    
    def __str__(self):
        return '[columnName={}, varName={}, methodName={}]'.format(self.column_name, self.var_name, self.method_name)


class Table(Model):

    def __init__(self, table_schema=None,
                 table_name=None,
                 table_comment=None,
                 engine=None,
                 row_format=None,
                 create_time=None,
                 table_collation=None):
        self.table_schema = table_schema
        self.table_name = table_name
        self.table_comment = table_comment
        self.engine = engine
        self.row_format = row_format
        self.create_time = create_time
        self.table_collation = table_collation
