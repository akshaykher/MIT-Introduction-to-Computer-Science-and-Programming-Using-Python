balance = 3329
annualInterestRate = 0.2
min_monthly_payment = 0
x = balance    
while balance > 0: 
    balance = x 
    month = 1
    min_monthly_payment = min_monthly_payment + 10
    while(month <=12):
        unbilled_amount = balance - min_monthly_payment
        interest = unbilled_amount*(annualInterestRate/12)
        balance = unbilled_amount + interest
        month = month + 1
print("Lowest Payment: " + str(min_monthly_payment))




