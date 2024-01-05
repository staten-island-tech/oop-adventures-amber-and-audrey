class Merchants():
    def __init__(self, name, products, price):
        self.name = name
        self.products = products
        self.price = price
    def sell(self, item):
        self.products.remove(item)
        print(f'You have purchased: {item}')
        print(self.products)
    def greeting():
        input("Welcome to the Merchant shop")

    

                 