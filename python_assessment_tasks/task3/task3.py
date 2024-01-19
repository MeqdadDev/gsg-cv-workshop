"""
Task 3:
Define a class Product with attributes like name, price, and quantity. 
Create an instance of the class and showcase its usage. 
"""
########### Solution ###########

from datetime import datetime

class Product(object):

    def __init__(self, name, price, quantity, pro_date, exp_date) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pro_date = pro_date
        self.exp_date = exp_date
    
    def get_name(self):
        return self.name
    
    def set_price(self, new_price):
        self.price = new_price
    
    def get_price(self):
        return self.price
    
    def set_quantity(self, new_qty):
        self.quantity = new_qty
    
    def get_quantitiy(self):
        return self.quantity
    
    def set_pro_date(self, new_pro_date: datetime):
        self.pro_date = new_pro_date
    
    def get_pro_date(self):
        return self.pro_date
    
    def set_exp_date(self, new_exp_date: datetime):
        self.exp_date = new_exp_date
    
    def get_exp_date(self):
        return self.exp_date
    
    def is_expired(self):
        current_date = datetime.now().date()
        return current_date > self.exp_date

############# Class usage #############

product1 = Product(name="Cheese",
                 price=20,
                 quantity=10,
                 pro_date=datetime(2024, 1, 1).date(),
                 exp_date=datetime(2024, 1, 31).date())

print(f"""a product {product1.get_name()} is created with the following details:\n
    - price = {product1.get_price()}\n
    - quantity = {product1.get_quantitiy()}\n
    - production date = {product1.get_pro_date()}\n
    - expiration date = {product1.get_exp_date()}\n
      """)

# Example: Changing quantity...

product1.set_quantity(15)
print("Product quantity is updated to", product1.get_quantitiy())


# Example: Checking product expiry

expiry = product1.is_expired()
# False means not expired
# True means expired product
print("Product expiry:", expiry)