class Market:
    def __init__(self, products):
        setattr(self, "cassa", 0)
        for product in products:
            setattr(self, product, products[product])

    def sell_product(self, name, quantity):
        price = getattr(self, name)
        self.cassa += price * quantity
        return { name: quantity }
    
    def add_product(self, name, price):
        setattr(self, name, price)
        return { name: price }

    def remove_product(self, name):
        delattr(self, name)
        return name


korzinka = Market({
    "non": 3500,
    "suv": 2000,
    "tuz": 2500
})


print(korzinka.add_product("kalbasa", 30000))
print(korzinka.cassa) 
print(korzinka.sell_product("kalbasa", 1))
print(korzinka.sell_product("non", 2)) 
print(korzinka.cassa) 
