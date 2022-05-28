a=[]
size=int(input("enter the size of list"))
for i in range(size):
    val=int(input("enter numbers"))
    a.append(val)
maxval=max(a)
print("max value in the list",maxval)
a.remove(maxval)
smax=max(a)
print("second maximum value in the list",smax)
a.remove(smax)
tmax=max(a)
print("third maximum",tmax)