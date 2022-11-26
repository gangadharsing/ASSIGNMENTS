# 9. Write a Python program to multiply all the items in a dictionary.

dict = {'d1':10,'d2':5,'d3':24, 'd4':4}
result=1
for key in dict:
    result=result * dict[key]
print(result)

