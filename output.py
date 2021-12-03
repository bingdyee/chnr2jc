import os, random
import settings, utils
from model import ModuleInfo, TableInfo
from mako.template import Template


class Contributor:

    def __init__(self, project):
        self.project = project
        self.root_dir = os.path.join(settings.output_dir, self.project.name)

    def output(self):
        pass

    @staticmethod
    def output_file(file, params, template_file):
        template = Template(filename=template_file)
        with open(file, 'w', encoding='utf8') as wf:
            wf.write(template.render(**params))

    def mk_module_dir(self, module):
        module_dir = os.path.join(self.root_dir, module)
        utils.mkdirs(module_dir)
        return module_dir

    def add_module(self, name, comment):
        module = ModuleInfo()
        module.common = True
        module.name = name.lower()
        module.comment = comment
        module.pro_name = self.project.name + '-' + module.name
        module.pkg_name = settings.base_package + '.'  + self.project.name + '.' + module.name
        self.project.modules.append(module)
        return module


class ProjectContributor:

    def __init__(self, project):
        self.project = project
        self.contributors = []

    def add_next(self, contributor: Contributor):
        self.contributors.append(contributor(self.project))
        return self
    
    def output(self):
        for contributor in self.contributors:
            contributor.output()


class ParentModuleContributor(Contributor):

    def __init__(self, project):
        super().__init__(project)

    def output(self):
        utils.rmdirs(self.root_dir)
        utils.copy(settings.mvn_assets_dir, self.root_dir)
        args = {
            'project': self.project,
            'modules': [module.pro_name for module in self.project.modules]
        }
        Contributor.output_file(os.path.join(self.root_dir, 'pom.xml'), args, settings.pom_xml_template)


class ModuleContributor(Contributor):

    def __init__(self, project):
        super().__init__(project)
        self.modules = [module for module in project.modules if not module.common]

    def output(self):
        for module in self.modules:
            module_dir = self.mk_module_dir(module.pro_name)
            module.dependencies += [module.pro_name for module in self.project.modules if module.common and module.name != settings.startup_module]
            args = { 'project': self.project, 'module': module }
            self.output_file(os.path.join(module_dir, 'pom.xml'), args, settings.subpom_xml_template)
            pkg_dir = os.path.join(module_dir, 'src/main/java', module.pkg_name.replace('.', '/'))
            utils.mkdirs(pkg_dir)
            self.output_file(os.path.join(pkg_dir, settings.constant_clz + settings.dot_java), args, settings.constant_template)
            for table in module.tables:
                args = {
                    'project': self.project,
                    'module': module,
                    'table': table,
                    'sv_uid': random.randint(100000000000000000, 999999999999999999)
                }
                self.output_entity(pkg_dir, args)
                self.output_mapper(pkg_dir, args)
                self.output_mapper_xml(args)
                self.output_vo(pkg_dir, args)
                self.output_dto(pkg_dir, args)
                self.output_query(pkg_dir, args)
                self.output_controller(pkg_dir, args)
                self.output_service(pkg_dir, args)

    def output_entity(self, base_dir, args):
        entity_dir = os.path.join(base_dir, settings.entity_package.replace('.', '/'))
        utils.mkdirs(entity_dir)
        self.output_file(os.path.join(entity_dir, args['table'].entity_name + settings.dot_java), args, settings.entity_template)

    def output_mapper(self, base_dir, args):
        mapper_dir = os.path.join(base_dir, settings.mapper_package.replace('.', '/'))
        utils.mkdirs(mapper_dir)
        self.output_file(os.path.join(mapper_dir, args['table'].mapper_clz + settings.dot_java), args, settings.mapper_template)
    
    def output_mapper_xml(self, args):
        xml_dir = os.path.join(self.root_dir, args['module'].pro_name, 'src/main/resources/mapper')
        utils.mkdirs(xml_dir)
        self.output_file(os.path.join(xml_dir, args['table'].mapper_xml_name + settings.dot_xml), args, settings.mapper_xml_template)

    def output_vo(self, base_dir, args):
        vo_dir = os.path.join(base_dir, settings.vo_package.replace('.', '/'))
        utils.mkdirs(vo_dir)
        self.output_file(os.path.join(vo_dir, args['table'].vo_clz + settings.dot_java), args, settings.vo_template)

    def output_dto(self, base_dir, args):
        dto_dir = os.path.join(base_dir, settings.dto_package.replace('.', '/'))
        utils.mkdirs(dto_dir)
        self.output_file(os.path.join(dto_dir, args['table'].dto_clz + settings.dot_java), args, settings.dto_template)

    def output_query(self, base_dir, args):
        query_dir = os.path.join(base_dir, settings.query_package.replace('.', '/'))
        utils.mkdirs(query_dir)
        self.output_file(os.path.join(query_dir, args['table'].query_clz + settings.dot_java), args, settings.query_template)

    def output_controller(self, base_dir, args):
        controller_dir = os.path.join(base_dir, settings.controller_package.replace('.', '/'))
        utils.mkdirs(controller_dir)
        self.output_file(os.path.join(controller_dir, args['table'].controller_clz + settings.dot_java), args, settings.controller_template)

    def output_service(self, base_dir, args):
        service_dir = os.path.join(base_dir, settings.service_package.replace('.', '/'))
        service_impl_dir = os.path.join(base_dir, settings.service_impl_package.replace('.', '/'))
        utils.mkdirs(service_dir)
        utils.mkdirs(service_impl_dir)
        self.output_file(os.path.join(service_dir, args['table'].service_clz + settings.dot_java), args, settings.service_template)
        self.output_file(os.path.join(service_impl_dir, args['table'].service_impl_clz + settings.dot_java), args, settings.service_impl_template)


class CommonModuleContributor(Contributor):
    """公共模块输出"""

    def __init__(self, project):
        super().__init__(project)
        self.module = self.add_module(settings.common_module, '公共模块')

    def output(self):
        module_dir = self.mk_module_dir(self.module.pro_name)
        args = { 'project': self.project, 'module': self.module }
        self.output_file(os.path.join(module_dir, 'pom.xml'), args, settings.subpom_xml_template)
        files = utils.dirs(settings.common_assets_dir)
        target_dir = os.path.join(module_dir, 'src/main/java', self.project.base_pkg.replace('.', '/'))
        for file in files:
            out_file = os.path.join(target_dir, settings.common_module, file.replace(settings.common_assets_dir, '')[1:])
            utils.mkdirs(out_file[0:out_file.rindex(os.sep)])
            self.output_file(out_file, args, file)


class StartupModuleContributor(Contributor):
    """启动模块输出"""

    def __init__(self, project):
        super().__init__(project)
        self.module = self.add_module(settings.startup_module, '启动模块')
        self.module.dependencies += [module.pro_name for module in project.modules if not module.common]

    def output(self):
        module_dir = self.mk_module_dir(self.module.pro_name)
        args = { 'project': self.project, 'module': self.module }
        self.output_file(os.path.join(module_dir, 'pom.xml'), args, settings.subpom_xml_template)
        src_target_dir = os.path.join(module_dir, 'src/main/java', self.project.base_pkg.replace('.', '/'))
        utils.mkdirs(src_target_dir)
        self.output_file(os.path.join(src_target_dir, self.project.full_name + 'Application.java'), args, settings.bootstrap_template)
        files = utils.dirs(settings.startup_assets_dir)
        res_target_dir = os.path.join(module_dir, 'src/main')
        for file in files:
            if file.endswith('.java'):
                out_file = os.path.join(src_target_dir, file.replace(settings.startup_assets_dir, '')[1:])
            if file.endswith('.yml'):
                out_file = os.path.join(res_target_dir, file.replace(settings.startup_assets_dir, '')[1:])
            utils.mkdirs(out_file[0:out_file.rindex(os.sep)])
            self.output_file(out_file, args, file)