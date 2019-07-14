# -*- coding: utf-8 -*-
from core.model import Model


class Column(Model):

    def __init__(self, tableName = None,
                        columnName = None,
                        dataType = None,
                        columnComment = None,
                        nullAble = None,
                        columnKey = None,
                        extra = None,
                        privileges = None):
        Model.__init__(self)
        
        self.tableName = tableName
        self.columnName = columnName
        self.dataType = dataType
        self.columnComment = columnComment
        self.nullAble = nullAble
        self.columnKey = columnKey
        self.extra = extra
        self.privileges = privileges
