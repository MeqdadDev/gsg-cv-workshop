"""
Task 4: (Based on Task 3)
Extend the Product class to include a method that calculates the total cost of a
certain quantity of that product.
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
    
    def calculate_product_cost(self, quantity=None):
        if quantity is None:
            quantity = self.quantity
        return quantity * self.price


############# Class usage #############

product1 = Product(name="Milk",
                 price=6,
                 quantity=50,
                 pro_date=datetime(2024, 1, 20).date(),
                 exp_date=datetime(2024, 2, 2).date())

print(f"""a product {product1.get_name()} is created with the following details:
    - price = {product1.get_price()}
    - quantity = {product1.get_quantitiy()}
    - production date = {product1.get_pro_date()}
    - expiration date = {product1.get_exp_date()}
      """)


# Example: Calculate total cost

print(f"Total cost for 5pcs of {product1.get_name()} is {product1.calculate_product_cost(5)} JOD")
print(f"Total cost for 10pcs of {product1.get_name()} is {product1.calculate_product_cost(10)} JOD")
print(f"Total cost for all available quantity of {product1.get_name()} ({product1.get_quantitiy()}pcs) is {product1.calculate_product_cost()} JOD")

print("#######################")
print("By: Meqdad A. Darwish")
print("Computer Vision Workshop by GSG")
