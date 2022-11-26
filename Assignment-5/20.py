# 20. You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

def square(list):
    ret = []
    for i in list:
        ret.append(i ** 2)
    return ret
list=[]
n=int(input("Enter the number of elements :"))
for i in range(0,n):
    ele = int(input())
    list.append(ele)
print(square(list))


