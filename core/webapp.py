# -*- coding: utf-8 -*-
from .jdbc import JdbcTemplate
from .mapper import Mapper

DB = Mapper(JdbcTemplate('root', 'root', 'code_generator'))

class TableList:

    def GET(self, table_name=None):
        return DB.select_table_list()

class TableColumn:

    def GET(self, table_name):
        return DB.select_table_column(table_name)

class Cogen:
    

    def GET(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs:
                print(k, v)
        return 'cogen'
