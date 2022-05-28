a=[]
size=int(input("enter the size of list"))
for i in range(size):
    val=int(input("enter the value"))
    a.append(val)
min=a[0]
for i in range(size):
    if (a[i]<min):
        min=a[i]
print("minimum number",min)


# n=[50,40,23,70,56,12,5,10,7]
# i=0
# min=0
# while i<len(n):
#     if min>n[i]:
#         min=n[i]
#     i=i+1
# print(min)
# i=0
# max=0
# while i<len(n):
#     if max<n[i]:
#         max=n[i]
#     i=i+1
# print(max)
