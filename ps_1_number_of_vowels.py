"""
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 

For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5
"""
#s = "akshay kher"
array_vowel = ["a","e","i","o","u"]
length = len(s)
vowel_count = 0

for i in range(length):
    if s[i] in array_vowel:
        vowel_count = vowel_count + 1
    else:
        vowel_count = vowel_count
print("Number of vowels: " + str(vowel_count))
    