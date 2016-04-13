balance = 999999
annualInterestRate = 0.18
Monthly_interest_rate = (annualInterestRate) / 12.0
low = balance / 12
high = (balance * (1 + Monthly_interest_rate)**12) / 12.0

while(abs(balance)>1):
    balance = 999999
    min_monthly_payment = (high+low)/2.0
    month = 1
    while(month <=12):
        unbilled_amount = balance - min_monthly_payment
        interest = unbilled_amount*(annualInterestRate/12)
        balance = unbilled_amount + interest
        month = month + 1
    print(balance)
    if balance > 0:
        low = min_monthly_payment
        high = high
    elif balance < 0:
        low = low
        high = min_monthly_payment
print("Lowest Payment: " + str(min_monthly_payment))


