# -*- coding: utf-8 -*-
import json


class ResponseEntity:

    def __init__(self, code=200, success=True, message='OK.', data=None):
        self.code = code
        self.success = success
        self.message = message
        self.data = data

    @staticmethod
    def error(code=500, message='Server error!'):
        return json.dumps(ResponseEntity(code, success=False, message=message).__dict__)

    @staticmethod
    def ok(data=None):
        return json.dumps(ResponseEntity(data=data).__dict__)
    
    def __str__(self):
        return "{'code': %d, 'success': %s, 'message': %s, 'data': %s}" % (self.code, self.success, self.message, self.data)

    def json(self):
        return json.dumps(self.__dict__)

