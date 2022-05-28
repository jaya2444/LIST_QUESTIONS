# 34. Write a Python program to remove all the values except integer values from a given
# array of mixed values.
# Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
# After removing all the values except integer values from the said array of mixed values:
# [12, 0]


a=[1,2,3,4,5,"deepa",6.3]
i=0
n=[]
while i<len(a):
    if type(a[i])==int:
        n.append(a[i])
    i=i+1
print(n)



# a=[1,2,3,4,5,"deepa",6.3]
# i=0
# while i<len(a):
#     if type(a[i])==float:
#         print(a[i])
#     i=i+1

    

# a=[1,2,3,4,5,"deepa",6.3]
# i=0
# while i<len(a):
#     if type(a[i])==str:
#         print(a[i])
#     i=i+1