a=[]
size=int(input("enter the size of list"))
for i in range(size):
    val=int(input("enter numbers"))
    a.append(val)
minval=min(a)
print("min value in the list",minval)
a.remove(minval)
smin=min(a)
print("second minimum value in the list",smin)
a.remove(smin)
tmin=min(a)
print("third minimum",tmin)