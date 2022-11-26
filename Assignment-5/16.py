# 16. Take inputs from user to make a list. Again take one input from user and search it in the list and delete that element, if found. Iterate over list using for loop.

numbers = []
x = int(input("Enter number of elements in list"))
print("Enter the elements")
for i in range(x):
    numbers.append(int(input()))
Num = int(input("The number to be deleted is "))
i = 0
for element in numbers:
    if (element == Num):
        numbers.pop(i)
        x = x - 1
        i = i - 1
    i = i + 1
print(numbers)
