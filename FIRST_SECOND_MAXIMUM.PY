a=[1,2,3,4]
i=0
max=0
b=[]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i=i+1
b.append(max)
print(b)
i=0
smax=0
c=[]
while i<len(a):
    if a[i]>smax and a[i]!=max:
        smax=a[i]
    i=i+1
c.append(smax)
print(c)