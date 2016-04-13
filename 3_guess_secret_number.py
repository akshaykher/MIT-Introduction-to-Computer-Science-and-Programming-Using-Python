high = 100
low = 0
flag = 100/2
user_input = 0

print("Please think of a number between 0 and 100!")

while(user_input != 'c'):
    print("Is your number " + str(flag) + "?")
    user_input = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if(user_input == 'c'):
        number = flag
    elif(user_input == 'l'):
        high = high
        low = flag
    elif(user_input == 'h'):
        high = flag
        low = low
    else:
        print("Sorry, I did not understand your input.")
    flag = (high+low)/2
    
print("Game over. Your secret number was: " + str(flag))

