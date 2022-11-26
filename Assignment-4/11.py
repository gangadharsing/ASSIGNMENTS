# 11. Write a Python function to reverses a string if it's length is a multiple of 4.
str=input("Enter the word: ")

if(len(str)%4==0):
    print(str[::-1])
else:
    print("cant")