# 30. Given a list of numbers, write a Python program to count positive and negative numbers in a List.
# Example:
# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3
# Iist2 = [-12, 14, 95, 3]
# Output: pos = 3, neg = 1



# a=[2,-7,5,-64,-14]
# i=0
# count=0
# count1=0
# while i<len(a):
#     if a[i]>0:
#         print(a[i],"positive numbers")
#         count=count+1
#     else:
#         print(a[i],"negative numbers")
#         count1=count1+1
#     i=i+1

# a=[2,-7,5,-64,-14]
a=[-12,14,95,3]
i=0
count=0
count1=0
while i<len(a):
    if a[i]>0:
        count=count+1
    else:
        count1=count1+1
    i=i+1
print("pos",count)
print("neg",count1)