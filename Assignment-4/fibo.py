n=int(input("Value for n"))

s1=0
s2=1
count =0


if n<= 0:
    print("No numbers")
elif n==1:
    print(s1)
else:
    while count<n:
        print(s1)
        ns=s1+s2
        s1=s2
        s2=ns
        count=count+1
