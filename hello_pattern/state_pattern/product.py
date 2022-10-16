class Product:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    
    def sell(self):
        self.amount -= 1
    
    def has_enough_amount(self, amount):
        return self.amount >= amount


product_lists = [
    dict(
        name="coffee",
        amount=3,
        price=10
    ),
    dict(
        name="cola",
        amount=5,
        price=15
    ),
]
PRODUCT_LIST = dict((p["name"], Product(**p)) for p in product_lists)
