# -*- coding: utf-8 -*-
import os
import random
import tenjin
from tenjin.helpers import *
from settings import TypeMapping
from .utils import list_files, format_time
from .mapper import *


full_capitalize = lambda name: name.title().replace('_', '')
lower_first = lambda name: name[0].lower() + name[1:]

def mkdirs(root):
    dirs = ['controller', 'service', 'mapper', 'pojo', 'api', 'service/impl', 'api/impl']
    [os.makedirs(os.path.join(root, path)) for path in dirs if not os.path.exists(os.path.join(root, path))]


class CodeGenerator:

    def __init__(self, table_name, package_name, module, template_path='templates', out_dir='temp', author='cogen'):
        self.table_name = table_name
        self.package_name = package_name
        self.module = module
        self.template_path = template_path
        self.out_dir = out_dir
        self.author = author
        self.content = None
        self._init()
    
    def _init(self):
        has_date, has_decimal, columns = self.get_columns(self.table_name)
        class_name = full_capitalize(self.table_name[self.table_name.index('_') + 1:])
        var_name = lower_first(class_name)
        self.content = {
            'tableName': self.table_name,
            'package': self.package_name,
            'module': self.module,
            'className': class_name,
            'varName': var_name,
            'columns': columns,
            'hasDate': has_date,
            'hasDecimal': has_decimal,
            'author': self.author,
            'datetime': format_time(fmt='%Y-%m-%d'),
            'comments': class_name,
            'serialVersionUID': 1,
        }

    def generate(self):
        engine = tenjin.Engine(path=[self.template_path])
        templates = list_files(self.template_path)
        target = os.path.join(self.out_dir, self.module)
        mkdirs(target)
        for template in templates:
            html = engine.render(template, self.content, layout=True)
            self.content['serialVersionUID'] = random.randint(999, 9999999999)
            file_name = self.get_out_path(template, self.content['className'] + template[0:-3], target)
            with open(file_name, 'wb') as f:
                f.write(html.encode('utf8'))

    def get_columns(self, table_name):
        columns = select_table_column(table_name)
        has_date, has_decimal = False, False
        for column in columns:
            column.data_type = TypeMapping[column.data_type]
            column.method_name = full_capitalize(column.column_name)
            column.var_name = lower_first(column.method_name)
            if column.data_type == 'BigDecimal':
                has_decimal = True
            if column.data_type == 'Date':
                has_date = True
        return has_date, has_decimal, columns

    def get_out_path(self, name, file_name, root):
        file_path = name
        if name.startswith('DO') or name.startswith('DTO') or name.startswith('VO'):
            file_path = os.path.join(root, 'pojo', file_name)
        if name.startswith('Api.'):
            file_path = os.path.join(root, 'api', file_name)
        if name.startswith('ApiImpl.'):
            file_path = os.path.join(root, 'api\\impl', file_name)
        if name.startswith('Service.'):
            file_path = os.path.join(root, 'service', file_name)
        if name.startswith('ServiceImpl.'):
            file_path = os.path.join(root, 'service\\impl', file_name)
        if name.startswith('Mapper'):
            file_path = os.path.join(root, 'mapper', file_name)
        if name.startswith('Controller'):
            file_path = os.path.join(root, 'controller', file_name)
        return file_path

    
