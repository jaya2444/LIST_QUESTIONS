# 41. Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)


# list=[[1,2],[2,4]]
# count=0
# for i in list:
#     count=count+1
#     count1=0
#     for i in list:
#         count1=count1+1
# print("(",count,end=",")
# print(count1,")")


# n=[[1,2],[2,4]]
# i=0
# c=0
# c1=0
# while i<len(n):
#     c=c+1
#     j=0
#     while j<len(n[i]):
#         c1=c1+1
#         j=j+1
#     i=i+1
# print("(",c,end=",")
# print(c1//2,")")


# n=[[0, 1, 2], [2, 4, 5]]
# i=0
# c=0
# c1=0
# while i<len(n):
#     c=c+1
#     j=0
#     while j<len(n[i]):
#         c1=c1+1
#         j=j+1
#     i=i+1
# print("(",c,end=",")
# print(c1//2,")")


# n=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# n=[[1,2],[2,4]]
n=[[0,1,2],[2,4,5]]
i=0
c=0
c1=0
while i<len(n):
    c=c+1
    j=0
    if i==0:
        while j<len(n[i]):
         c1=c1+1
         j=j+1
    i=i+1
print("(",c,end=",")
print(c1,")")


# by laSt method we can do all the questions