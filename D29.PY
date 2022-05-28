# 29. Remove empty List from List
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

list=[5, 6, [], 3, [], [], 9]
b=[]
for i in list:
    if i!=[]:
        b.append(i)
print(b)