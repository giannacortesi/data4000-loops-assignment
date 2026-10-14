# 1. Retail Checkout Simulation
# Skills: while loop, input validation, lists
 
prices = []  # list that stores every item price
 
print("Enter the price of each item. Enter 0 when you are done.")
 
price = float(input("Item price: "))
 
# Keep asking until the customer enters 0
while price != 0:
    if price < 0:
        # Input validation: reject negative prices
        print("Price cannot be negative. Try again.")
    else:
        prices.append(price)
    price = float(input("Item price: "))
 
# Only calculate results if at least one item was entered
if len(prices) > 0:
    total = sum(prices)
    count = len(prices)
    average = total / count
    print(f"Number of items bought: {count}")
    print(f"Total purchase amount: ${total:,.2f}")
    print(f"Average item cost: ${average:,.2f}")
else:
    print("No items were entered.")