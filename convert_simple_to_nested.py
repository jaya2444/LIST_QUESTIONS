l=[2,4,6,7,9,8,7,6,5,4,43,33,9]
i=0
b=[]
while i<len(l)-2:
    b.append(l[i:i+2])
    i=i+2
print(b)