# 15. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ).
# Print average and product of all numbers.

summ = 0
count = 0
product=1
raw_input=input("Press Q to Quit")
while raw_input != 'q':
    product=product*int(raw_input)
    summ = summ+int(raw_input)
    count=count+1
    raw_input = input("Press Q to Quit")
print("avreage",summ/count)
print("Product",product)


