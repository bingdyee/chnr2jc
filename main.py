# -*- coding: utf-8 -*-
from http.server import HTTPServer
from core.dispatcher import DispatcherHandler, RestController
from core.jdbc import JdbcTemplate
from core.mapper import *


@RestController
class UserController:

    urls = {
        '/index': 'index',
        '/login': 'login'
    }

    def __init__(self):
        print('create')

    def index(self, table_name=None):
        results = select_table_list(table_name)
        return [result.json() for result in results]

    def login(self, name):
        return select_table_column(name).json()


if __name__ == '__main__':
    port = 8002
    DispatcherHandler.init(globals())
    httpd = HTTPServer(('', port), DispatcherHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()
