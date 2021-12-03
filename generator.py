import output
from chnr_parser import ChnrParser
from output import ProjectContributor


if __name__ == '__main__':
    chnr_file = 'docs/deliver.chnr.json'
    # chnr_file = 'docs/archetype-demo.chnr.json'

    ProjectContributor(ChnrParser(chnr_file).parse()) \
        .add_next(output.ParentModuleContributor) \
        .add_next(output.CommonModuleContributor) \
        .add_next(output.StartupModuleContributor) \
        .add_next(output.ModuleContributor) \
        .output()

