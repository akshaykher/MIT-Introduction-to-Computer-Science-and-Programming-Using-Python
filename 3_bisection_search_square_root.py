number = int(raw_input("Enter the number: "))
high = number
low = 0
flag = number/2.0

while(abs(flag**2 - number) > 0.01):
    if flag**2 > number:
        low = low
        high = flag
    elif flag**2 < number:
        low = flag
        high = high
    flag = (high+low)/2.0
print("")
print("The square root of " + str(number) + " is " + str(flag))

