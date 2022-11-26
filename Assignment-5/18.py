# 18. From the two list obtained in previous question, make new lists, containing only numbers which are divisible by
# 4, 6, 8, 10, 3, 5, 7 and 9 in separate lists.

even=[]
odd=[]
prime=[]
for num in range(1,101):
   if num % 2 == 0:
        even.append(num)
   else:
        odd.append(num)
   for i in range(2, (num//2+1)):
        if(num % i == 0):
           break
   else :
       prime.append(num)
by=[4,6,8,10,3,5,7,9]
for i in range(len(by)):
    list=[]
    print("The Even Number divisible by",by[i])
    for x in range(len(even)):
        if (even[x]%by[i]==0):
           list.append(even[x])
    print(list)
for i in range(len(by)):
    list=[]
    print("The Odd Number divisible by",by[i])
    for x in range(len(odd)):
        if (odd[x]%by[i]==0):
            list.append(odd[x])
    print(list)