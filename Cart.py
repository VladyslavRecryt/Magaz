class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock -= quantity

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}, Stock: {self.stock}"


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.stock >= quantity:
            product.update_stock(quantity)
            self.items.append((product, quantity))
        else:
            print(f"Недостатньо наявності для {product.name}")

    def remove_product(self, product):
        self.items = [(p, q) for p, q in self.items if p != product]

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def show_cart(self):
        for product, quantity in self.items:
            print(f"{product.name} x{quantity} - {product.price * quantity} UAH")


# Приклад використання:
product1 = Product("Ноутбук", 15000, 5)
product2 = Product("Навушники", 2000, 10)

cart = Cart()
cart.add_product(product1, 1)
cart.add_product(product2, 2)

cart.show_cart()
print("Total:", cart.total_price())
