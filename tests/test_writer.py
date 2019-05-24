from hcl.writer import *


class Foo(HclBase):
    NAME = "Foo"

    def __init__(self):
        self._hcl_label = 'foo_label'
        self.string = 'Some String'
        self.num = 128
        self.bool = True


class Bar(HclBase):
    NAME = "Bar"

    def __init__(self):
        self._hcl_label = 'bar_label'
        self.foo = Foo()
        self.arr = ['I', 'am', 'a', 'pirate', '!']
        self.map = {'test': 1, 'set': 2, 'tes': 3}


print(dumps(Foo()))
print(dumps(Bar()))
