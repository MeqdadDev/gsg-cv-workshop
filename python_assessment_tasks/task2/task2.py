"""
Task 2:
Implement a function that takes a dictionary of products and their prices.
Calculate the total cost of a given basket of products and apply a discount of 10%.
Print the discounted total.
"""
########### Solution ###########

def cashier(client_cart: dict):
    total_cost = sum(client_cart.values())
    cost_after_discount = total_cost - (total_cost * 0.1)
    return total_cost, cost_after_discount



products_cart = {"mouse": 10.0,
                 "keyboard": 20.5,
                 "monitor": 400.0,
                 "speaker": 45.0}



if __name__ == "__main__":
    total, discounted_total = cashier(products_cart)
    print("Total cost =", total, "JOD")
    print("Total cost with discount =", discounted_total, "JOD")
    
    print("By: Meqdad A. Darwish")
    print("Computer Vision Workshop by GSG")
