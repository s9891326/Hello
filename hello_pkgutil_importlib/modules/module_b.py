from hello_pkgutil_importlib.libs.base import Base


class ModuleB(Base):
    def __init__(self):
        super(ModuleB, self).__init__()
        self.name = 'ModuleB'

