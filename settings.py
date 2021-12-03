"""
生成器基础配置
"""

dot_java = '.java'
dot_xml = '.xml'

# 全局配置
base_package = 'com.shudazy'
author = 'shudazy'
version = '1.0.0'
exclude_tables = []
ignore_prefix = True
output_dir = './temp'
mvn_assets_dir = './templates/mvn'
common_assets_dir = './templates/common'
startup_assets_dir = './templates/startup'
common_module = 'common'
startup_module = 'startup'
common_fields = ['updated_dept', 'updated_user', 'updated_time', 'updated_done']
tree_field_suffix = '_root'

# 模块配置
entity_template = 'templates/entity.java.vm'
dto_template = 'templates/dto.java.vm'
vo_template = 'templates/vo.java.vm'
query_template = 'templates/query.java.vm'
mapper_template = 'templates/mapper.java.vm'
mapper_xml_template = 'templates/mapper.xml.vm'
service_template = 'templates/service.java.vm'
service_impl_template = 'templates/serviceImpl.java.vm'
controller_template = 'templates/controller.java.vm'
pom_xml_template = 'templates/pom.xml.vm'
subpom_xml_template = 'templates/subpom.xml.vm'
constant_template = 'templates/constant.java.vm'
bootstrap_template = 'templates/bootstrap.java.vm'

# 包配置
entity_package = 'pojo.entity'
dto_package = 'pojo.dto'
vo_package = 'pojo.vo'
query_package = 'pojo.query'
mapper_package = 'mapper'
service_package = 'service'
service_impl_package = 'service.impl'
controller_package = 'controller'


# 类名后缀
entity_suffix = ''
dto_suffix = 'DTO'
vo_suffix = 'VO'
query_suffix = 'Query'
mapper_suffix = 'Mapper'
service_suffix = 'Service'
service_impl_suffix = 'ServiceImpl'
controller_suffix = 'Controller'
constant_clz = 'ModuleConstant'
mapper_xml_suffix = 'Mapper'

# 字段映射
field_map = {
    'BigDecimal': 'java.lang.BigDecimal',
    'LocalDateTime': 'java.time.LocalDateTime',
    'LocalDate': 'java.time.LocalDate',
    'Date': 'java.util.Date'
}

enable_sql_output = False
dict_sql_template = """"""
enum_sql_template = """"""