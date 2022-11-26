# 6. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda
# Orginal list: [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# Numbers of the above list divisible by nineteen or thirteen: [19, 65, 57, 39, 152, 190]

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
print("Orginal list:")
print(nums)
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums))
print("Numbers of the above list divisible by 19 or 13:")
print(result)