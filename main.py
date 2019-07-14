# -*- coding: utf-8 -*-
# import web
# import core.webapp, core.jdbc, core.mapper


# urls = (
#   '/tableList', 'core.webapp.TableList',
#   '/table_name=(.*)', 'core.webapp.TableColumn',
#   '/cogen?a=(.*)', 'core.webapp.Cogen'
# )


# if __name__ == "__main__": 
#     app = web.application(urls, globals())
#     app.run()

from http.server import HTTPServer
from webpy.dispatcher import DispatcherHandler, RestController
from core.jdbc import JdbcTemplate
from core.mapper import Mapper


@RestController
class UserController:

    mapper = Mapper(JdbcTemplate('root', 'root', 'code_generator'))

    urls = {
        '/index': 'index',
        '/login': 'login'
    }

    def __init__(self):
        print('create')

    def index(self):
        return self.mapper.select_table_list()

    def login(self, name):
        return 'Login success. ' + name



if __name__ == '__main__':
    port = 8002
    
    httpd = HTTPServer(('', port), DispatcherHandler)
    print("Starting simple_httpd on port: " + str(httpd.server_port))
    httpd.serve_forever()