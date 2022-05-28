# 4. Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

n=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=0
min=len(n[1])
c=[]
k=[]
while i<len(n):
    if len(n[i])>max:
        max=len(n[i])
        c=n[i]
    if len(n[i])<min:
        min=len(n[i])
        k=n[i]
    i=i+1
print("max",max,c)
print("min",min,k)



