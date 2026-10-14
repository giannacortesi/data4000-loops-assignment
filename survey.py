# 2. Market Survey Analyzer
# Skills: for loop, dictionaries, counting
 
# Fake survey data: each entry is one customer's preference
preferences = ["coffee", "tea", "coffee", "soda"]
 
counts = {}  # dictionary: product -> number of votes
 
# Count how many people chose each product
for choice in preferences:
    if choice in counts:
        counts[choice] += 1
    else:
        counts[choice] = 1
 
total_responses = len(preferences)
 
# Print a market-share style summary
print("Market share summary:")
for product in counts:
    percent = counts[product] / total_responses * 100
    print(f"{product}: {round(percent, 1):g}%")