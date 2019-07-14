# -*- coding: utf-8 -*-
from http.server import HTTPServer
from core.dispatcher import DispatcherHandler, RestController
from core.jdbc import JdbcTemplate
from core.mapper import *


@RestController
class MainController:

    urls = {
        '/tableList': 'table_list',
        '/tableColumn': 'table_column',
        '/cogen', 'generate_code'
    }

    def table_list(self, table_name=None):
        results = select_table_list(table_name)
        return [result.json() for result in results]

    def table_column(self, table_name):
        results = select_table_column(table_name)
        return [result.json() for result in results]

    def generate_code(self):
        return ''


if __name__ == '__main__':
    port = 8002
    DispatcherHandler.init(globals())
    httpd = HTTPServer(('', port), DispatcherHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()
