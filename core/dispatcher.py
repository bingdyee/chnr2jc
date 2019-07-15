# -*- coding: utf-8 -*-
import json
import socket
import urllib
import functools
import traceback
from http.server import SimpleHTTPRequestHandler
from http import HTTPStatus
from .result import ResponseEntity, File
from .model import Model


HandleMapping = {  }
Mappers = []

def RestController(cls):
    global HandleMapping
    if hasattr(cls, 'urls'):
        urls = getattr(cls, 'urls')
        for k, v in urls.items():
            if HandleMapping.get(k) is not None:
                return
            HandleMapping[k] = {'class': cls, 'method': v}
    return cls


class DispatcherHandler(SimpleHTTPRequestHandler):

    """HTTP request dispatcher class.
    RESTful API
    """
    _globals = None

    def __init__(self, req, client_addr, server):
        SimpleHTTPRequestHandler.__init__(self, req, client_addr, server)

    @staticmethod
    def init(_globals):
        DispatcherHandler._globals = _globals
        return DispatcherHandler

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = ''
                self.request_version = ''
                self.command = ''
                self.send_error(HTTPStatus.REQUEST_URI_TOO_LONG)
                return
            if not self.raw_requestline:
                self.close_connection = True
                return
            if not self.parse_request():
                return
            self.dispatcher()
            self.wfile.flush()
        except socket.timeout as e:
            self.log_error("Request timed out: %r", e)
            self.close_connection = True
            return

    def handle_params(self):
        path = urllib.parse.unquote(self.path)
        if '?' in path:
            path, params = path.split('?')
            ps = urllib.parse.parse_qsl(params)
            params = { p[0]:p[1] for p in ps }
        else:
            length = self.headers['content-length']
            params = self.rfile.read(int(length)).decode('utf-8') if length else '{}'
            params = json.loads(params)
        return path, params

    def send_headers(self, content_type='application/json;charset=utf-8', disposition=None):
        self.send_response(200)
        self.send_header("Content-type", content_type)
        if disposition:
            self.send_header('Content-Disposition', disposition)
        self.end_headers()

    def dispatcher(self):
        try:
            path, params = self.handle_params()
            mapping = HandleMapping.get(path)
            if mapping is None:
                result = ResponseEntity.error(404, 'Not Found')
            else:
                result = getattr(mapping.get('class'), mapping.get('method'))(mapping.get('class'), **params)
                if isinstance(result, File):
                    self.send_headers(content_type=result.content_type, disposition=result.disposition)
                    with open(result.path, 'rb') as rf:
                        self.copyfile(rf, self.wfile)
                    return
        except:
            traceback.print_exc()
            result = ResponseEntity.error('Unknow Error')
        self.send_headers()
        self.wfile.write(result.encode('utf8'))
        
        


    
        