# 4. List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 90



a=[6,1,3,5,6,3,1]
i=0
p=[]
while i<len(a):
    h=a[i]
    if h not in p:
        p.append(h)
    i=i+1
print(p)
i=0
product=1
while i<len(p):
    product=product*p[i]
    i=i+1
print(product)



# l=[6,1,3,5,6,3,1]
# i=0
# p=1
# a=[]
# while i<len(l):
#     if l[i] not in a:
#         a.append(l[i])
#         p=p*a[i]
#     i=i+1
# print(p)