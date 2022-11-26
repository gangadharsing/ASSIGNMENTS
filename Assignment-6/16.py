# 16. Write a Python program to find the highest 3 values in a dictionary.

from heapq import nlargest
dict = {'a':5, 'b':587, 'c': 56,'d':40, 'e':587, 'f': 200}
largest = nlargest(3, dict, key=dict.get)
print(largest)
