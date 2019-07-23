# -*- coding: utf-8 -*-
import os
import optparse
import random
import tenjin
from tenjin.helpers import *
from core.utils import list_files, format_time
from core.mapper import *
from settings import TypeMapping


full_capitalize = lambda name: name.title().replace('_', '')
lower_first = lambda name: name[0].lower() + name[1:]


def get_columns(table_name):
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


def get_out_path(name, file_name, root, zteng=False):
    file_path = name
    if name.startswith('DO'):
        file_path = os.path.join(root, 'pojo\\po' if zteng else 'pojo',
                                 file_name.replace('DO', '') if zteng else file_name)
    if name.startswith('DTO'):
        file_path = os.path.join(root, 'pojo', file_name)
    if name.startswith('VO'):
        file_path = os.path.join(root, 'pojo\\vo' if zteng else 'pojo', file_name)
    if name.startswith('Api.'):
        file_path = os.path.join(root, 'service\\ao' if zteng else 'api',
                                 file_name.replace('Api', 'AoService') if zteng else file_name)
    if name.startswith('ApiImpl.'):
        file_path = os.path.join(root, 'service\\ao\\impl' if zteng else 'api\\impl',
                                 file_name.replace('Api', 'AoService') if zteng else file_name)
    if name.startswith('Service.'):
        file_path = os.path.join(root, 'service\\bo' if zteng else 'service', file_name)
    if name.startswith('ServiceImpl.'):
        file_path = os.path.join(root, 'service\\bo\\impl' if zteng else 'service\\impl', file_name)
    if name.startswith('Mapper'):
        file_path = os.path.join(root, 'mapper', file_name)
    if name.startswith('Controller'):
        file_path = os.path.join(root, 'controller', file_name)
    return file_path


def mkdirs(root, zteng=False):
    dirs = ['controller', 'service\\bo', 'mapper', 'pojo\\po', 'pojo\\vo', 'service\\ao', 'service\\bo\\impl',
            'service\\ao\\impl'] if zteng else ['controller', 'service', 'mapper', 'pojo', 'api', 'service/impl',
                                                'api/impl']
    [os.makedirs(os.path.join(root, path)) for path in dirs if not os.path.exists(os.path.join(root, path))]


def usage():
    parser = optparse.OptionParser("usage: %prog -t <table name> -m <module> -p <package name> [-o target output dir] "
                                   "[-u author]")
    parser.add_option("-t", dest="table_name", type="string", help="specify table")
    parser.add_option("-m", dest="module", type="string", help="specify module name")
    parser.add_option("-p", dest="package_name", type="string", help="specify package name")
    parser.add_option("-o", dest="target", type="string", help="specify package name", default='temp')
    parser.add_option("-u", dest="author", type="string", help="specify package name", default='devuser')
    (options, args) = parser.parse_args()
    if options.table_name is None or options.module is None or options.package_name is None:
        parser.print_help()
        quit(-1)
    return options.table_name, options.module, options.package_name, options.target, options.author


def main(zteng=True):
    table_name, module, package_name, target, author = usage()
    has_date, has_decimal, columns = get_columns(table_name)
    class_name = full_capitalize(table_name[table_name.index('_') + 1:])
    var_name = lower_first(class_name)
    context = {
        'tableName': table_name,
        'package': package_name,
        'module': module,
        'className': class_name,
        'varName': var_name,
        'columns': columns,
        'hasDate': has_date,
        'hasDecimal': has_decimal,
        'author': author,
        'datetime': format_time(fmt='%Y-%m-%d'),
        'comments': class_name,
        'serialVersionUID': 1,
        'zteng': zteng
    }
    src = 'templates\\zteng' if zteng else 'templates'
    engine = tenjin.Engine(path=[src])
    templates = list_files(src)
    root = os.path.join(target, module)
    mkdirs(root, zteng=zteng)
    for template in templates:
        if zteng and template.startswith('DTO'):
            continue
        html = engine.render(template, context, layout=True)
        context['serialVersionUID'] = random.randint(999, 9999999999)
        file_name = get_out_path(template, class_name + template[0:-3], root, zteng=zteng)
        with open(file_name, 'wb') as f:
            f.write(html.encode('utf8'))


if __name__ == '__main__':
    # python main.py -t tb_account -m account -p org.warless.cogen -o tmp -u yubb
    main()
