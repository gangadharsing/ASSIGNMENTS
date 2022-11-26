# 10.  Write a Python program to sort a given mixed list of integers and strings using lambda. Numbers must be sorted before strings.
# Original list: [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]
# Sort the said mixed list of integers and strings: [1, 10, 12, 19, 'blue', 'green', 'green', 'red', 'white']

def mixed(list):
    list.sort(key=lambda e: (isinstance(e, str), e))
    return list
list = [19,'red',12,'green','blue', 10,'white','green',1]
print("Original list:")
print(list)
print("Sort the mixed list of integers and strings:")
print(mixed(list))
