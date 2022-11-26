# 13. Write a Python program to check whether a string starts with specified characters.
string1=input("Enter the string : ")
string2=input("Enter the character :")
if(string1.startswith(string2)):
    print("Yes It starts with "+string2)
else:
    print("No it does not starts with "+string2)