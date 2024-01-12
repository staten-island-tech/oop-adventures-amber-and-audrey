class Merchants():
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self, item):
        self.products.remove(item)
        print(f'You have purchased: {item}')
        print(self.products)
    def greeting(self, products):
        self.products = products
        input("Welcome to the Merchant shop")
        print(products)






    

                 