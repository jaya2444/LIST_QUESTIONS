l=[[3,4,5],[5,6,7],[8,9,0]]
i=0
b=[]
while i<len(l):
    j=0
    while j<len(l[i]):
        a=l[i][j]
        b.append(a)
        j=j+1
    i=i+1
print(b)

