# 4. Write a Python script to check if a given key already exists in a dictionary.

d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x=int(input('enter the value'))
if x in d:
      print('Key is present in the dictionary')
else:
      print('Key is not present in the dictionary')