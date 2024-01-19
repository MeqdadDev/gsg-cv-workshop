""" 
Task 1: 
Given a list of sales amounts for a week, calculate the total sales and average
sales. Print the results. 
"""
########### Solution ###########

def calculate_sales(sales:list):
    total = 0
    total = sum(sales)
    # OR..... looping over each item
    # for s in sales:
    #     total += s
    print(f"Total weekly sales = {total:.2f} JOD")
    print(f"Average weekly sales = {total/len(sales):.2f} JOD")

weekly_sales = [200.0, 300.0, 170.2, 240.7, 330.8, 405.5]

if __name__ == "__main__":
    calculate_sales(weekly_sales)
    print("By: Meqdad A. Darwish")
    print("Computer Vision Workshop by GSG")

