# 11. Write a Python program to sort a dictionary by key.

dict = {'mango': 3, 'orange': 2, 'apple': 5, 'banana': 1}
for key in sorted(dict):
    print("%s: %s" % (key, dict[key]))
