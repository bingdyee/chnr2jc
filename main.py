# -*- coding: utf-8 -*-
import optparse
from core.generator import CodeGenerator

def usage():
    parser = optparse.OptionParser("usage: %prog -t <table name> -m <module> -p <package name> [-o target output dir] "
                                   "[-u author]")
    parser.add_option("-t", dest="table_name", type="string", help="table name")
    parser.add_option("-m", dest="module", type="string", help="module name")
    parser.add_option("-p", dest="package_name", type="string", help="package name")
    parser.add_option("-o", dest="target", type="string", help="package name", default='temp')
    parser.add_option("-u", dest="author", type="string", help="author name", default='devuser')
    (options, args) = parser.parse_args()
    if options.table_name is None or options.module is None or options.package_name is None:
        parser.print_help()
        quit(-1)
    return options.table_name, options.module, options.package_name, options.target, options.author


def main(args=None):
    table_name, module, package_name, target, author = usage()
    cogen = CodeGenerator(table_name, package_name, module, out_dir=target, author=author)
    cogen.generate()


if __name__ == '__main__':
    main()
