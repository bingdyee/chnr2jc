# -*- coding: utf-8 -*-
import json
from datetime import datetime

class Model:

    def __init__(self, **props):
        self.data = props

    def __call__(self, key):
        return self.get(key)

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.set(key, value)

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def json(self):
        for k, v in self.data.items():
            if isinstance(v, datetime):
                self.data[k] = '2019-10-10'
        return json.dumps(self.data)
