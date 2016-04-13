"""
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 

For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""
#s = 'tibobobbbobbbobobbboobbo'
count = 0

for i in range(len(s)):
    print(i)
    if s[i] == "b" and i<=(len(s)-3):
        if(s[i+1] =="o" and s[i+2] == "b"):
            count = count + 1
        else:
            count = count
            
print("Number of times bob occurs is:" + str(count))