
list_x=[]
list_y=[]
n=int(input("Enter the number of coordinates"))
for x in range(0,n):
    list_x.append(int(input("Enter the x value:")))
    list_y.append(int(input("Enter the y values:")))
list_p=[]
mini=min(min(list_x),min(list_y))
if mini < 0:
    to_add = 0-(mini)
    for x in range(0,n):
        list_x[x]=int(list_x[x])+to_add
        list_y[x]=int(list_y[x])+to_add
    for x in range(0, n):
        print("(", list_x[x], ",", list_y[x], ")")
else:
    print("All the coordinates are positive")



