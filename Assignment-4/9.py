# 9. Write a Python program to remove the nth index character from a nonempty string.
def remove(str, n):
    first_part = str[:n]
    last_part = str[n + 1:]
    return first_part + last_part

str1=input("Enter the string")
index=int(input("Entert the index"))
print(remove(str1, index))

