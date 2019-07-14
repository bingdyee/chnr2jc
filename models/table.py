# -*- coding: utf-8 -*-
from core.model import Model


class Table(Model):

    def __init__(self):
        Model.__init__(self)
        self.tableSchema = None
        self.tableName = None
        self.tableComment = None
        self.engine = None
        self.rowFormat = None
        self.createTime = None
        self.tableCollation = None