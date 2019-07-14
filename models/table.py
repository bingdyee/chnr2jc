# -*- coding: utf-8 -*-
from core.model import Model


class Table(Model):

    def __init__(self, tableSchema=None, 
                        tableName=None, 
                        tableComment=None, 
                        engine=None, 
                        rowFormat=None, 
                        createTime=None, 
                        tableCollation=None):
        Model.__init__(self)
        self.tableSchema = tableSchema
        self.tableName = tableName
        self.tableComment = tableComment
        self.engine = engine
        self.rowFormat = rowFormat
        self.createTime = createTime
        self.tableCollation = tableCollation