class NotExistItemErrorExeception(Exception):
    pass


class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} | {self.price}"

    def code(self):
        return f"{self.name}-123"

    def multiply_price(self):
        self.price = self.price * 2


class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def contains_items(self) -> bool:
        return len(self.items) > 0

    def remove_item(self, item: Item):
        self.items.remove(item)

    def get_item(self, item: Item):
        if item not in self.items:
            raise NotExistItemErrorExeception('Item does not exists')
        return self.items[self.items.index(item) - 1]

    def total(self) -> int:
        return sum([item.price for item in self.items])
