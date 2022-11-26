# 9. Write a Python program to find the elements of a given list of strings that contain specific substring using lambda.
# Original list: ['red', 'black', 'white', 'green', 'orange']
# Substring to search: ack Elements of the said list that contain specific substring: ['black']
# Substring to search: abc Elements of the said list that contain specific substring: []

def substring(str1, str):
    result = list(filter(lambda x: str in x, str1))
    return result
colors = ["red", "black", "white", "green", "orange"]
print("Original list:")
print(colors)
str = "ack"
print("Substring to search:")
print(str)
print("Elements of the said list that contain specific substring:")
print(substring(colors, str))
str = "abc"
print("Substring to search:")
print(str)
print("Elements of the said list that contain specific substring:")
print(substring(colors, str))

