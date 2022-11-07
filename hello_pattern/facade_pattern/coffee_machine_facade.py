from hello_pattern.facade_pattern.coffee_machine import CoffeeMachine
from hello_pattern.facade_pattern.ice_cream_machine import IceCreamMachine


class CoffeeMachineFacade:
    def make_latte(self):
        coffee = CoffeeMachine()
        
        return [coffee.add_coffee_beans(), coffee.grind(), coffee.brew(), coffee.stir_with_milk()]

