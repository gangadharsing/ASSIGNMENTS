# string=input("Enter the coordinate without braket in following format   x1,y1 x2,y2 x3,y3 ......  xn,yn :")
# coordinates=string.split(" ")
# list_of_coordinates=[]
# for x in coordinates:
#     list_of_coordinates.append(coordinates.split(","))
# intlist=[eval(i) for i in list_of_coordinates]
# lowest=(min(min(list_of_coordinates)))
# updated_coordinates=[]
# if int(lowest)<0:
#     to_add=0-int(lowest)
#     for x in range(0,len(list_of_coordinates)):
#         updated_coordinates.append(intlist[x]+to_add)
# else:
#     print("There is no negative")
#     print(list_of_coordinates)

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



