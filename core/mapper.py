# -*- coding: utf-8 -*-
from .jdbc import JdbcTemplate


TABLE_LIST_SQL = ("""
    SELECT
        table_schema AS tableSchema,
        table_name AS tableName,
        table_comment AS tableComment,
        engine,
        row_format AS rowFormat,
        create_time AS createTime,
        table_collation AS tableCollation
    FROM
        information_schema.tables
    WHERE
        table_schema=(SELECT DATABASE()) {}
""", "AND table_name LIKE CONCAT('%%', %s, '%%')")


TABLE_COLUMN_SQL = """
    SELECT
        table_name AS tableName,
        column_name AS columnName,
        data_type AS dataType,
        column_comment AS columnComment,
        is_nullable AS nullAble,
        column_key AS columnKey,
        extra,
        privileges
      FROM
        information_schema.columns
      WHERE
        table_name=%s AND table_schema=(SELECT DATABASE())
"""

class Mapper:

    def __init__(self, jdbc):
        self.jdbc = jdbc

    def select_table_list(self, table_name=None):
        sql = TABLE_LIST_SQL[0].format('' if table_name is None  else TABLE_LIST_SQL[1])
        d = self.jdbc.select(sql, table_name)
        print(type(d[0]['createTime']))
        return self.jdbc.select(sql, table_name)

    def select_table_column(self, table_name):
        return self.jdbc.select(TABLE_COLUMN_SQL, table_name)


