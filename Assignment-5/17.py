# 17. Using range(1,101), make three list,
# one containing all even numbers
# one containing all odd numbers
# One containing only prime numbers..

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
print('even',even)
print('odd', odd)
print('prime', prime)