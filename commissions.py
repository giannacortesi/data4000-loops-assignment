# 4. Sales Commission Calculator
# Skills: for loop, functions
 
def calculate_commission(sales_amount, rate=0.10):
    """Return the commission earned (default 10%) on a sales amount."""
    return sales_amount * rate
 
 
sales = {"Alice": 5000, "Bob": 7000, "Carol": 3000}
 
# Build a dictionary of commissions using the function
commissions = {}
for employee in sales:
    commissions[employee] = calculate_commission(sales[employee])
 
# Sort employee names from highest commission to lowest
ranked = sorted(commissions, key=commissions.get, reverse=True)
 
print("===== COMMISSION LEADERBOARD =====")
rank = 1
for employee in ranked:
    print(f"{rank}. {employee:<8} ${commissions[employee]:,.2f}")
    rank += 1