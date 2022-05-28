# 24. Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]


n=[1,2,3,1,2,2,]
i=0
a=[]
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    i=i+1
print(a)
