# 10. Startup Pitch Deck Visualizer (ASCII Style)
# Skills: nested loops, string multiplication
 
# Projected revenue by year (in $100,000s); one # = $100,000
revenue = {1: 3, 2: 5, 3: 8, 4: 12, 5: 15}
 
print("Projected Revenue by Year (each # = $100,000)")
 
# String multiplication: "#" * 3 gives "###"
for year in revenue:
    print(f"Year {year}: {'#' * revenue[year]}")
 
print()
 
# Same chart built with a nested loop instead of string multiplication
for year in revenue:
    bar = ""
    for block in range(revenue[year]):
        bar += "#"
    print(f"Year {year}: {bar} (${revenue[year] * 100000:,})")