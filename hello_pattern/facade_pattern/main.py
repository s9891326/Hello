from hello_pattern.facade_pattern.coffee_machine_facade import CoffeeMachineFacade
from hello_pattern.facade_pattern.ice_cream_machine_facade import IceCreamMachineFacade


class Program:
    def make_ice_cream(self):
        return IceCreamMachineFacade().make_ice_cream()
    
    def make_latte(self):
        return CoffeeMachineFacade().make_latte()


if __name__ == '__main__':
    program = Program()
    print(program.make_ice_cream())
    print(program.make_latte())
