# 5. Write a Python program to check whether a given string is number or not using Lambda.

num = lambda q: q.replace('.','',1).isdigit()
print(num('26587'))
print("Print checking numbers:")
num1 = lambda r: num(r[1:]) if r[0]=='-' else num(r)
print(num1('-16.4'))
print(num1('-0.11'))

