# 8. Customer Loyalty Tiers
# Skills: conditionals, dictionaries, loops
 
# Each customer's total purchase amount
customers = {
    "Alice": 5200,
    "Bob": 800,
    "Carol": 1500,
    "Dave": 4999,
    "Eve": 7300,
    "Frank": 1000
}
 
tier_counts = {"Bronze": 0, "Silver": 0, "Gold": 0}
 
for customer in customers:
    amount = customers[customer]
    if amount >= 5000:
        tier = "Gold"
    elif amount >= 1000:
        tier = "Silver"
    else:
        tier = "Bronze"
    tier_counts[tier] += 1
    print(f"{customer}: ${amount:,.2f} -> {tier}")
 
print("\nTier summary:")
for tier in tier_counts:
    print(f"{tier}: {tier_counts[tier]} customers")