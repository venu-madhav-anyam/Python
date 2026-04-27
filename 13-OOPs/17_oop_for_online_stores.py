class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_items(self, item_name, quantity, price):
        if item_name in self.items:
            self.items[item_name][0] += quantity
        else:
            self.items[item_name] = [quantity, price]

    def remove_items(self,item_name, quantity):
        if item_name in self.items:
            if quantity > self.items[self.items][0]:
                del self.items[item_name]
            else:
                self.items[item_name][0] -= quantity

    def total_price(self):
        return sum(tot * price for tot, price in self.items.values())


s = ShoppingCart()
s.add_items('Book',2,200)
s.add_items('Pen',5,20)
print(s.total_price())

    