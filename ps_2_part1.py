balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
month = 1
paid_total = 0

while(month <=12):
    min_monthly_payment = round(balance * monthlyPaymentRate,2)
    unbilled_amount = balance - min_monthly_payment
    interest = unbilled_amount*(annualInterestRate/12)
    balance = round(unbilled_amount + interest,2)
    paid_total = paid_total + min_monthly_payment
    print("Month: " + str(month))
    print("Minimum monthly payment: " + str(min_monthly_payment))
    print("Remaining balance: " + str(balance))
    month = month + 1
print("Total paid: " + str(paid_total))
print("Remaining balance: " + str(balance))
