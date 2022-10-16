from hello_pattern.facade_pattern.ice_cream_machine import IceCreamMachine


class IceCreamMachineFacade:
    def make_ice_cream(self):
        ice_cream = IceCreamMachine()
        
        return [ice_cream.add_ingredients(), ice_cream.stir(), ice_cream.chill(), ice_cream.squeeze()]

