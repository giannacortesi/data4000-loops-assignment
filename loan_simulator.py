
# 6. Bank Loan Repayment Simulator
# Skills: while loops, math, functions
 
def monthly_interest(balance, annual_rate_percent):
    """Interest charged for one month on the current balance."""
    return balance * (annual_rate_percent / 100) / 12
 
 
loan_amount = float(input("Loan amount: "))
annual_rate = float(input("Annual interest rate (%): "))
monthly_payment = float(input("Monthly payment: "))
 
balance = loan_amount
 
# If the payment doesn't cover the first month's interest, the loan never ends
if monthly_payment <= monthly_interest(balance, annual_rate):
    print("Your payment is too small to ever pay off this loan.")
else:
    months = 0
    while balance > 0:
        balance += monthly_interest(balance, annual_rate)  # add interest
        balance -= monthly_payment                         # subtract payment
        months += 1
        if balance < 0:
            balance = 0  # final payment may be smaller than the full payment
        print(f"Month {months}: balance ${balance:,.2f}")
 
    years = months // 12
    remaining = months % 12
    print(f"The loan is paid off in {months} months ({years} years, {remaining} months).")