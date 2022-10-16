from abc import ABC, abstractmethod


class StateInterface(ABC):
    @abstractmethod
    def insert_money(self):
        pass
    
    @abstractmethod
    def refund_money(self):
        pass
    
    @abstractmethod
    def press_button(self):
        pass
    
    @abstractmethod
    def dispense(self):
        pass


class StandbyState(StateInterface):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    def insert_money(self, money=0):
        print(f"you insert money: {money}")
        self.vending_machine.set_has_money_state()
    
    def refund_money(self):
        print('You have not insert a money')
    
    def press_button(self):
        pass
    
    def dispense(self):
        pass


class HasMoneyState(StateInterface):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    def insert_money(self):
        pass
    
    def refund_money(self):
        print(f"Refund money {self.vending_machine.get_refund_money()}")
        self.vending_machine.set_standby_state()
    
    def press_button(self):
        self.vending_machine.set_sold_state()
    
    def dispense(self):
        pass


class SoldState(StateInterface):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    def insert_money(self):
        pass
    
    def refund_money(self):
        pass
    
    def press_button(self):
        pass
    
    def dispense(self):
        if self.vending_machine.has_enough_amount():
            if self.vending_machine.is_correct_price():
                self.vending_machine.sold()
                print(f"Refund money is {self.vending_machine.get_refund_money()}")
                self.vending_machine.set_standby_state()
            else:
                print(f"Not enough money, please insert more money. "
                      f"Product price: {self.vending_machine.product.price}, "
                      f"Insert money: {self.vending_machine.money}")
                self.vending_machine.set_has_money_state()
        else:
            print("Not enough Product or insert money is not correct")
            self.vending_machine.set_sold_out_state()


class SoldOutState(StateInterface):
    def __init__(self, vending_machine):
        self.vending_machine = vending_machine
    
    def insert_money(self):
        pass
    
    def refund_money(self):
        pass
    
    def press_button(self):
        pass
    
    def dispense(self):
        pass
