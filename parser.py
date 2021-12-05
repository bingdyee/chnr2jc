import json
import settings
from pypinyin import Style, pinyin, lazy_pinyin
from utils import full_capitalize, lower_first
from model import ProjectInfo, ModuleInfo, TableInfo, TableField, DictInfo, EnumInfo


class ChnrParser:

    def __init__(self, path, ignore_prefix=True):
        self.common_fields = settings.common_fields
        self.ignore_prefix = ignore_prefix
        self.exclude_tables = settings.exclude_tables
        with open(path, 'r', encoding='utf8') as rf:
            self.chnr = json.load(rf)
        self.dbid = self.chnr['profile']['default']['db']
        for support in self.chnr['profile']['dataTypeSupports']:
            if support['defKey'] == 'JAVA':
                self.jid = support['id']
                break
        self.project = ProjectInfo()
        self.project.version = settings.version
        self.project.author = settings.author
        self.project_modules = []

    def parse(self):
        groups = self.chnr['viewGroups']
        entities = self.chnr['entities']
        self.project.name = self.chnr['name'].lower()
        self.project.full_name = full_capitalize(self.chnr['name'])
        self.project.describe = self.chnr['describe']
        self.project.base_pkg = settings.base_package + '.' + self.project.name
        for group in groups:
            module = ModuleInfo()
            module.name = group['defKey'].lower()
            module.comment = group['defName']
            module.constant_clz = settings.constant_clz
            module.pro_name = self.project.name + '-' + module.name
            module.pkg_name = settings.base_package + '.' + self.project.name + '.' + module.name
            self.project.modules.append(module)
            group_entities = []
            for entity_id in group['refEntities']:
                group_entities += [entity for entity in entities if entity['id'] == entity_id]
            tables, dicts = self.parse_module(group['defKey'], group_entities)
            module.tables += tables
            module.dicts += set(dicts)
        return self.project

    def parse_module(self, group, entities):
        tables, dicts = [], []
        group = group.lower()
        for entity in entities:
            table_name = entity['defKey'].lower()
            if table_name in self.exclude_tables:
                continue
            table = TableInfo()
            table.name = table_name
            if table.name.endswith(settings.tree_field_suffix):
                table.is_tree = True
            table.comment = entity['defName']
            table.entity_name = full_capitalize(table.name[table.name.index('_'):] if self.ignore_prefix else table.name)
            table.prop_name = lower_first(table.entity_name)
            group_pkg = self.project.base_pkg + '.' + group + '.'
            table.entity_pkg = group_pkg + settings.entity_package
            table.dto_pkg = group_pkg + settings.dto_package
            table.vo_pkg = group_pkg + settings.vo_package
            table.query_pkg = group_pkg + settings.query_package
            table.mapper_pkg = group_pkg + settings.mapper_package
            table.service_pkg = group_pkg + settings.service_package
            table.service_impl_pkg = group_pkg + settings.service_impl_package
            table.controller_pkg = group_pkg + settings.controller_package
            table.dto_clz = table.entity_name + settings.dto_suffix
            table.vo_clz = table.entity_name + settings.vo_suffix
            table.mapper_clz = table.entity_name + settings.mapper_suffix
            table.service_clz = table.entity_name + settings.service_suffix
            table.query_clz = table.entity_name + settings.query_suffix
            table.service_impl_clz = table.entity_name + settings.service_impl_suffix
            table.controller_clz = table.entity_name + settings.controller_suffix
            table.mapper_xml_name = table.entity_name + settings.mapper_xml_suffix
            table.vo_prop_name = lower_first(table.vo_clz)
            table.dto_prop_name = lower_first(table.dto_clz)
            table.query_prop_name = lower_first(table.query_clz)
            table.mapper_prop_name = lower_first(table.mapper_clz)
            table.service_prop_name = lower_first(table.service_clz)
            table.service_impl_prop_name = lower_first(table.service_impl_clz)
            has_pk = False
            for field in entity['fields']:
                table_field = TableField()
                table_field.name = field['defKey'].lower()
                if table_field.name in self.common_fields:
                    table_field.common = True
                table_field.comment = field['defName']
                table_field.prop_name = lower_first(full_capitalize(table_field.name))
                table_field.not_null = field['notNull']
                if not has_pk and field['primaryKey']:
                    table_field.primary_key = field['primaryKey']
                    has_pk = True
                self.parse_field(field['domain'], table_field)
                table.fields.append(table_field)
                if field.get('refDict') and field['refDict'] != '':
                    dict_info = self.parse_dict(group, field['refDict'])
                    dicts.append(dict_info)
                pkg = settings.field_map.get(table_field.type)
                if pkg: table.pkgs.add(pkg) 
            tables.append(table)
        return tables, dicts

    def parse_field(self, domain_id, table_field):
        domains = [did for did in self.chnr['domains'] if domain_id == did['id']]
        domain = domains[0]
        table_field.length = domain['len']
        table_field.scale = domain['scale']
        for mapping in self.chnr['dataTypeMapping']['mappings']:
            if mapping['id'] == domain['applyFor']:
                table_field.type = mapping[self.jid]
                table_field.column_type = mapping[self.dbid]
                break

    def parse_dict(self, module, dict_id):
        _dict = [_dict for _dict in self.chnr['dicts'] if _dict['id'] == dict_id][0]
        dict_info = DictInfo()
        dict_info.name = _dict['defName']
        dict_info.sign = module.upper() + '_' + _dict['defKey']
        dict_info.intro = _dict['intro']
        for enum in _dict['items']:
            enum_info = EnumInfo()
            enum_info.sign = dict_info.sign + '_' + ChnrParser.get_enum_suffix(enum['defName'])
            enum_info.name = enum['defName']
            enum_info.code = enum['defKey']
            enum_info.intro = enum['intro']
            enum_info.sort = enum['sort']
            enum_info.attr1 = enum['attr1']
            enum_info.attr2 = enum['attr2']
            enum_info.attr2 = enum['attr3']
            dict_info.enums.append(enum_info)
        return dict_info

    def get_enum_suffix(enum_name, bound=5):
        suffix = ''.join(lazy_pinyin(enum_name))
        # 名称长度大于 bound 时，采用拼音首字母
        if len(enum_name) > bound:
            pys = pinyin(enum_name, style=Style.INITIALS, strict=False)
            pys = [p[0] for p in pys]
            suffix = ''.join(pys)
        return suffix.upper()
