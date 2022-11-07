from hello_pattern.state_pattern.vending_machine import VendingMachine


def order_one(vending_machine, price: int, product_name: str):
    vending_machine.insert_money(price)
    vending_machine.press_button(product_name)
    print(f'Number of {product_name} the vending machine have : {vending_machine.get_amount()}')


def order_two(vending_machine, price: int, product_name: str):
    vending_machine.insert_money(price)
    vending_machine.press_button(product_name)
    vending_machine.insert_money(price)
    vending_machine.press_button(product_name)
    print(f'Number of {product_name} the vending machine have : {vending_machine.get_amount()}')


def order_coffee_but_not_correct_money(vending_machine, price: int, product_name: str):
    vending_machine.insert_money(price)
    vending_machine.press_button(product_name)
    print(f'number of {product_name} the vending machine have : {vending_machine.get_amount()}')


def refund_money(vending_machine, price: int):
    vending_machine.insert_money(price)
    vending_machine.refund_money()
    print(f'How much we insert after we refund: {vending_machine.get_refund_money()}')


def refund_money_fail(vending_machine, price: int, product_name: str):
    vending_machine.insert_money(price)
    vending_machine.press_button(product_name)
    vending_machine.refund_money()


if __name__ == '__main__':
    order_one(VendingMachine(), 15, "cola")
    order_two(VendingMachine(), 15, "cola")
    order_coffee_but_not_correct_money(VendingMachine(), 5, "coffee")
    refund_money(VendingMachine(), 15)
    refund_money_fail(VendingMachine(), 10, "cola")
    refund_money_fail(VendingMachine(), 15, "cola")
