from hello_pkgutil_importlib.libs.base import Base


class ModuleA(Base):
    def __init__(self):
        super(ModuleA, self).__init__()
        self.name = 'ModuleA'

