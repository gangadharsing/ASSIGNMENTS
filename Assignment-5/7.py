# 7. Write a Python program that counts the number of elements within a list that are greater than 30.

list=[]
count=0
n=int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
    if ele>30:
        count=count+1
print(count)
