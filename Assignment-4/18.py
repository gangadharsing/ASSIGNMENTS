# 18. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

a = input("Enter the string")
print(a)
maketrans = a.maketrans
a = a.translate(maketrans(',.', '.,'))
print(a)