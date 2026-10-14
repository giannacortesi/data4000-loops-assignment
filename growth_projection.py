# 9. Business Growth Projection
# Skills: for loops, math
 
initial_revenue = float(input("Initial revenue: "))
growth_rate = float(input("Annual growth rate (%): "))
 
revenue = initial_revenue
 
print(f"\n{'Year':<6}{'Revenue':>16}")
print("-" * 22)
 
# Each year, revenue grows by the growth rate
for year in range(1, 11):
    revenue = revenue * (1 + growth_rate / 100)
    print(f"{year:<6}${revenue:>15,.2f}")