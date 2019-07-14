# -*- coding: utf-8 -*-
import json
import socket
import urllib
import functools
import traceback
from http.server import BaseHTTPRequestHandler
from http import HTTPStatus
from .result import ResponseEntity

HandleMapping = {  }
Mappers = []

def RestController(cls):
    global HandleMapping
    if hasattr(cls, 'urls'):
        urls = getattr(cls, 'urls')
        for k, v in urls.items():
            if HandleMapping.get(k) is not None:
                raise
            HandleMapping[k] = {'class': cls, 'method': v}
    return cls




class DispatcherHandler(BaseHTTPRequestHandler):

    _globals = None

    def __init__(self, req, client_addr, server):
        BaseHTTPRequestHandler.__init__(self, req, client_addr, server)

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
            self.wfile.write(self.dispatcher())
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

    def dispatcher(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json;charset=utf-8")
        self.end_headers()
        try:
            path, params = self.handle_params()
            mapping = HandleMapping.get(path)
            if mapping is not None:
                method = getattr(mapping.get('class'), mapping.get('method'))
                rs = method(mapping.get('class'), **params)
                return ResponseEntity.ok(rs).encode('utf-8')
            return ResponseEntity.error(404, 'Not Found').encode('utf-8')
        except:
            traceback.print_exc()
            return ResponseEntity.error('Unknow Error').encode('utf-8')
        
        


    
        