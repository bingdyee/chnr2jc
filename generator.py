import tenjin
import pymysql
from tenjin.helpers import *
from utils.commons import format_time, list_files


TypeMapping = {
    ''
}

SQL = """
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

table_name = 'tb_account'

conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='code_generator', charset='utf8mb4')

with conn.cursor(cursor=pymysql.cursors.DictCursor) as cursor:
    cursor.execute(SQL, table_name)
    results = cursor.fetchall()

columns = [row for row in results]
for column in columns:
    pass
print(columns)

var_name = table_name[table_name.index('_') + 1:]
class_name = var_name.capitalize()

context = {
    'package': 'org.warless.cogen',
    'module': 'account',
    'className': class_name,
    'author': 'Noa',
    'datetime': format_time(),
    'columns': ['A', 'B'],
    'varName': var_name,
    'serialVersionUID': 5464545646415,
    'comments': table_name
}
engine = tenjin.Engine(path=['templates'])

html = engine.render('DO.java', context)
print(html)

conn.close()