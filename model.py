class ProjectInfo:

    def __init__(self):
        self.name = None
        self.full_name = None
        self.describe = None
        self.base_pkg = None
        self.version = '1.0.0'
        self.author = None
        self.modules = []
        self.since = '2021-11-10'
    
    def __str__(self) -> str:
        return 'ProjectInfo{name: %s, basePkg: %s, describe: %s, version: %s}' % (self.name, self.base_pkg, self.describe, self.version)


class ModuleInfo:

    def __init__(self):
        self.common = False
        self.name = None
        self.comment = None
        self.pro_name = None
        self.pkg_name = None
        self.tables = []
        self.dicts = []
        self.dependencies = []
        self.constant_clz = None

    def __str__(self) -> str:
        return 'ModuleInfo{name: %s, comment: %s, proName: %s, pkgName: %s}' % (self.name, self.comment, self.pro_name, self.pkg_name)


class TableInfo:

    def __init__(self):
        self.name = None
        self.comment = None
        self.fields = []
        self.entity_name = None
        self.prop_name = None
        self.pkgs = set()
        self.query_pkg = None
        self.entity_pkg = None
        self.dto_pkg = None
        self.vo_pkg = None
        self.mapper_pkg = None
        self.controller_pkg = None
        self.service_pkg = None
        self.service_impl_pkg = None
        self.dto_clz = None
        self.vo_clz = None
        self.mapper_clz = None
        self.service_clz = None
        self.query_clz = None
        self.service_impl_clz = None
        self.controller_clz = None
        self.mapper_xml_name = None
        self.vo_prop_name = None
        self.dto_prop_name = None
        self.query_prop_name = None
        self.mapper_prop_name = None
        self.service_prop_name = None
        self.service_impl_prop_name = None
        self.is_tree = False

    def __str__(self):
        return 'TableInfo{name: %s comment: %s entityName: %s}' % (self.name, self.comment, self.entity_name)


class TableField:

    def __init__(self):
        self.name = None
        self.comment = None
        self.type = None
        self.prop_name = None
        self.column_type = None
        self.not_null = False
        self.length = None
        self.scale = None
        self.primary_key = False
        self.fill = False
        self.common = False

    def __str__(self):
        return 'TableField{name: %s, comment: %s, type: %s, propName: %s, columnType: %s, notNull: %s, primaryKey: %s, ' \
               'length: %s, scale: %s}' % \
               (self.name, self.comment, self.type, self.prop_name, self.column_type, self.not_null, self.primary_key, self.length, self.scale)


class DictInfo:

    def __init__(self):
        self.sign = None
        self.name = None
        self.intro = None
        self.enums = []

    def __str__(self):
        return 'DictInfo{sign: %s, name: %s, intro: %s}' % (self.sign, self.name, self.intro)

    def __hash__(self) -> int:
        return hash(self.sign)
    
    def __eq__(self, o: object) -> bool:
        return o.sign == self.sign


class EnumInfo:

    def __init__(self):
        self.sign = None
        self.name = None
        self.code = None
        self.sort = 0
        self.intro = None
        self.attr1 = None
        self.attr2 = None
        self.attr3 = None

    def __str__(self):
        return 'EnumInfo{sign: %s, name: %s, code: %s, intro: %s}' % (self.sign, self.name, self.code, self.intro)
