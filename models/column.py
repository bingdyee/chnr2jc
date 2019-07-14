# -*- coding: utf-8 -*-
from core.model import Model


class Column(Model):

    def __init__(self):
        Model.__init__(self)
        self.tableName = None
        self.columnName = None
        self.dataType = None
        self.columnComment = None
        self.nullAble = None
        self.columnKey = None
        self.extra = None
        self.privileges = None
