# -*- coding: utf-8 -*-
from .jdbc import mapper
from models import Table, Column
from typing import List

TABLE_LIST_SQL = ("""
    SELECT
        table_schema AS tableSchema,
        table_name AS tableName,
        table_comment AS tableComment,
        engine AS engine,
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
        extra as extra,
        privileges as privileges
      FROM
        information_schema.columns
      WHERE
        table_name=%s AND table_schema=(SELECT DATABASE())
"""

@mapper
def select_table_list(table_name: str = None) -> List[Table]:
    return TABLE_LIST_SQL[0].format('' if table_name is None  else TABLE_LIST_SQL[1])

@mapper
def select_table_column(table_name: str) -> List[Column]:
    return TABLE_COLUMN_SQL


