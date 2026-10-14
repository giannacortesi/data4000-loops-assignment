
# 7. Simple Supply Chain Tracker
# Skills: nested loops, lists of dictionaries
 
warehouses = [
    {"name": "Warehouse A", "inventory": {"apples": 100, "bananas": 150}},
    {"name": "Warehouse B", "inventory": {"apples": 200, "bananas": 100}}
]
 
totals = {}  # product -> total stock across all warehouses
 
# Outer loop: each warehouse
for warehouse in warehouses:
    # Inner loop: each product in that warehouse's inventory
    for product in warehouse["inventory"]:
        quantity = warehouse["inventory"][product]
        if product in totals:
            totals[product] += quantity
        else:
            totals[product] = quantity
 
print("Total stock across the supply chain:")
for product in totals:
    print(f"{product}: {totals[product]}")