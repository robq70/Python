from cart import *

phone1 = Phone("Phone X", 1000, "red")
tv1 = TV("TV Y", 2000, 65)
test = TV("TV LG", 2100, 75)

cart = Cart()
cart.addProduct(phone1)
cart.addProduct(tv1)
cart.addProduct(tv1)
cart.addProduct("test") 
print(cart)