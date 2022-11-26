# 12. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.
str1 = input("Enter the String :")
count = 0
for letter in str1[:4]:
    if letter.upper() == letter:
        count += 1
if count >= 2:
    print(str1.upper())
print(str1)
