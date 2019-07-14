# -*- coding: utf-8 -*-
import json
from datetime import datetime


class Model:

    def __init__(self, data=None):
        self.data = data

    def json(self):
        rs = self.__dict__ if self.data is None else self.data
        rs.pop('data')
        for k, v in rs.items():
            rs[k] = v.strftime('%Y-%m-%d %H:%M:%S') if isinstance(v, datetime) else v
        return rs
