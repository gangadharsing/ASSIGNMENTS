# 19. From a list containing ints, strings and floats, make three lists to store them separately

w=[4, 5, 1.1, 'abcd', 3.4, 'xyz', 2]
x=[]
y=[]
z=[]
for i in w:
    if type(i)==int:
        x.append(i)
    elif type(i)==float:
        y.append(i)
    elif type(i)==str:
        z.append(i)
print(x)
print(y)
print(z)

