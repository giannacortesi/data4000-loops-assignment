# DATA 4000: Python Assignment (Loops)

Python 3.x, developed in VS Code.

| File | Description |
|------|-------------|
| `checkout.py` | While loop collects item prices until 0 is entered; prints total, average, and item count. |
| `survey.py` | Counts survey responses in a dictionary and prints market share percentages. |
| `expenses.py` | Nested loops total expenses by category and print an expense summary report. |
| `commissions.py` | Function calculates 10% commission; prints a leaderboard ranked by commission. |
| `portfolio.py` | Calculates portfolio value; bonus simulates a week of random +/-5% daily price changes. |
| `loan_simulator.py` | While loop simulates monthly repayments and reports months to pay off the loan. |
| `supply_chain.py` | Nested loops total each product's stock across all warehouses. |
| `loyalty_tiers.py` | Assigns Bronze/Silver/Gold tiers and counts customers in each. |
| `growth_projection.py` | Projects revenue over 10 years from a starting revenue and growth rate. |
| `pitch_chart.py` | Draws an ASCII bar chart of projected revenue using `#`. |

## Assumptions
- Inputs are entered as plain numbers (no `$` or commas).
- `checkout.py` rejects negative prices and stops when 0 is entered.
- `loan_simulator.py` takes an annual interest rate (%) and applies it monthly (rate / 12). If the payment can't cover the interest, it reports that the loan can never be paid off.
- `growth_projection.py`: Year 1 is revenue after the first year of growth.
- `portfolio.py` results differ each run because daily changes are random.

## Sample run (checkout.py)

    Item price: 10
    Item price: 20
    Item price: 0
    Number of items bought: 2
    Total purchase amount: $30.00
    Average item cost: $15.00 
