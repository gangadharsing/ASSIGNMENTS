# 12.  Write a Python program to get the maximum and minimum value in a dictionary.

dict = {'x':50, 'y':5, 'z': 56, 'a':46}
keymax = max(dict.keys(), key=(lambda k: dict[k]))
keymin = min(dict.keys(), key=(lambda k: dict[k]))
print('Maximum Value: ',dict[keymax])
print('Minimum Value: ',dict[keymin])

