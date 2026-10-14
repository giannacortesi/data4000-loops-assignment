# 3. Expense Report Categorizer
# Skills: nested loops, dictionaries
 
expenses = {
    "Travel": [500, 200],
    "Meals": [40, 60, 30],
    "Supplies": [100]
}
 
grand_total = 0
 
print("===== EXPENSE SUMMARY REPORT =====")
 
# Outer loop goes through each category
for category in expenses:
    category_total = 0
    # Inner loop goes through each expense in that category
    for amount in expenses[category]:
        category_total += amount
    print(f"{category:<10} ${category_total:>8,.2f}")
    grand_total += category_total
 
print("-" * 31)
print(f"{'TOTAL':<10} ${grand_total:>8,.2f}")