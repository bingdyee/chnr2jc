import tenjin
from tenjin.helpers import *

context = {
    'packageName': 'org.warless.cogen',
    'module': 'test',
    'className': 'Test',
    'columns': ['A', 'B']
}

engine = tenjin.Engine(path=['templates'])

html = engine.render('Test.java', context)
print(html)