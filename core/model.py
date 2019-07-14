# -*- coding: utf-8 -*-
import json
from datetime import datetime


class Model:

    def __init__(self, data=None, **props):
        data = {} if data is None else data
        self._data =  {**data, **props}

    def __call__(self, key):
        return self.get(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def set(self, key, value):
        self._data[key] = value

    def get(self, key):
        return self._data.get(key)

    def json(self):
        for k, v in self._data.items():
            if isinstance(v, datetime):
                self._data[k] = v.strftime('%Y-%m-%d %H:%M:%S')
        for k, v in self.__dict__.items():
            if not k.startswith('_'):
                self._data[k] = v.strftime('%Y-%m-%d %H:%M:%S') if isinstance(v, datetime) else v
        return json.dumps(self._data)