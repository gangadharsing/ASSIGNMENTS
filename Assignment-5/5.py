# 5. Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish

print("Input integers to calculate sum and average. Input 0 to exit.")
count = 0
sum = 0.0
number = 1
while number != 0:
    number = int(input(""))
    sum = sum + number
    count += 1
if count == 0:
    print("Input some numbers")
else:
    print("sum of the above numbers:",sum)
    print("Average and Sum of the above numbers: ", sum / (count - 1))


