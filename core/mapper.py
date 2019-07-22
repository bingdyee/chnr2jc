# -*- coding: utf-8 -*-
from typing import List
from .jdbc import mapper
from .models import Table, Column


TABLE_LIST_SQL = ("""
    SELECT
        table_schema AS table_schema,
        table_name AS table_name,
        table_comment AS table_comment,
        engine AS engine,
        row_format AS row_format,
        create_time AS create_time,
        table_collation AS table_collation
    FROM
        information_schema.tables
    WHERE
        table_schema=(SELECT DATABASE()) {}
""", "AND table_name LIKE CONCAT('%%', %s, '%%')")


@mapper
def select_table_list(table_name: str = None) -> List[Table]:
    return TABLE_LIST_SQL[0].format('' if table_name is None else TABLE_LIST_SQL[1])


@mapper
def select_table_column(table_name: str) -> List[Column]:
    return """
        SELECT
            table_name AS table_name,
            column_name AS column_name,
            data_type AS data_type,
            column_comment AS column_comment,
            is_nullable AS nullable,
            column_key AS column_key,
            extra as extra,
            privileges as privileges
          FROM
            information_schema.columns
          WHERE
            table_name=%s AND table_schema=(SELECT DATABASE()) ORDER BY ordinal_position
    """

