from hello_pattern.state_pattern.product import PRODUCT_LIST
from hello_pattern.state_pattern.state import StandbyState, StateInterface, HasMoneyState, SoldState, SoldOutState


class VendingMachine:
    def __init__(self):
        self._money = 0
        self._refund_money = 0
        self.product = None
        self.product_list = PRODUCT_LIST
        self._standby_state = StandbyState(self)
        self._has_money_state = HasMoneyState(self)
        self._sold_state = SoldState(self)
        self._sold_out_state = SoldOutState(self)
        self._state = self._standby_state
    
    def insert_money(self, money: int):
        self.set_refund_money(money)
        self.money = money
        self._state.insert_money(money)
    
    def press_button(self, product_name: str):
        print(f"You press button: {product_name}")
        self._set_product(product_name)
        self._state.press_button()
        self._state.dispense()
    
    def refund_money(self):
        self.money = 0
        self._state.refund_money()
    
    def set_has_money_state(self):
        self._set_state(self._has_money_state)
    
    def set_sold_state(self):
        self._set_state(self._sold_state)
    
    def set_sold_out_state(self):
        self._set_state(self._sold_out_state)
    
    def set_standby_state(self):
        self._set_state(self._standby_state)
    
    def _set_product(self, product_name: str):
        product = self.product_list.get(product_name)
        if product:
            self.product = product
        else:
            raise ValueError(f"No this product: {product_name}")
    
    def _set_state(self, state: StateInterface):
        self._state = state
    
    def has_enough_amount(self):
        return self.product.amount > 0
    
    def is_correct_price(self):
        return self.money >= self.product.price
    
    def sold(self):
        self.product.amount -= 1
        self.set_refund_money(self.money - self.product.price)
        print(f"You product {self.product.name} is coming ~")
    
    def get_amount(self):
        return self.product.amount
    
    @property
    def money(self):
        return self._money
    
    @money.setter
    def money(self, money):
        self._money = money
    
    def get_refund_money(self):
        return self._refund_money
    
    def set_refund_money(self, money):
        self._refund_money = money
