import pkgutil
import importlib

from hello_pkgutil_importlib.libs.base import Base


def load_modules():
    for finder, name, _ in pkgutil.iter_modules(['modules']):
        try:
            importlib.import_module('{}.{}'.format(finder.path, name))
        except Exception as e:
            print('Can not import {}'.format(name))


def main():
    load_modules()

    for cls in Base.__subclasses__():
        instance = cls()
        instance.run()


if __name__ == '__main__':
    main()
