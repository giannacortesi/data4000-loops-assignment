# 5. Stock Portfolio Tracker
# Skills: dictionaries, loops, nested dictionaries
import random
 
portfolio = {
    "AAPL": {"shares": 10, "price": 170},
    "TSLA": {"shares": 4, "price": 250},
    "AMZN": {"shares": 2, "price": 130}
}
 
 
def total_value(stocks):
    """Add up shares * price for every stock."""
    total = 0
    for ticker in stocks:
        total += stocks[ticker]["shares"] * stocks[ticker]["price"]
    return total
 
 
print(f"Starting portfolio value: ${total_value(portfolio):,.2f}")
 
# Bonus: simulate a week of random daily price changes (+/- 5%)
for day in range(1, 8):
    for ticker in portfolio:
        change = random.uniform(-0.05, 0.05)  # random value between -5% and +5%
        portfolio[ticker]["price"] *= (1 + change)
    print(f"Day {day}: ${total_value(portfolio):,.2f}")