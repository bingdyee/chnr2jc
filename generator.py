import output
from parser import ChnrParser


def main():
    chnr_file = 'docs/archetype-demo.chnr.json'
    parser = ChnrParser(chnr_file)
    project = parser.parse()
    output.ProjectContributor(project) \
        .add_next(output.ParentModuleContributor) \
        .add_next(output.CommonModuleContributor) \
        .add_next(output.StartupModuleContributor) \
        .add_next(output.ModuleContributor) \
        .output()


if __name__ == '__main__':
    main()
