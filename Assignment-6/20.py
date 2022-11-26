# 20. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]

a = [10, 20, 30]
b = [40, 50, 60]
print(a)
print(b)
a[:0] =b
print(a)