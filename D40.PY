# 40. Write a Python program to sum two or more lists, the lengths of the lists may be
# different.
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]


# n=[[1, 2, 4], [2, 4, 4], [1, 2]]
# i=0
# sum=0
# sum1=0
# sum2=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if j==0:
#             sum=sum+n[i][j]
#         elif j==1:
#             sum1=sum1+n[i][j]
#         else:
#             sum2=sum2+n[i][j]
#         j=j+1
#     i=i+1
# a.append(sum)
# a.append(sum1)
# a.append(sum2)
# print(a)

# n=[[1], [2, 4, 4], [1, 2], [4]]
# i=0
# sum=0
# sum1=0
# sum2=0
# a=[]
# while i<len(n):
#     j=0
#     while j<len(n[i]):
#         if j==0:
#             sum=sum+n[i][j]
#         elif j==1:
#             sum1=sum1+n[i][j]
#         else:
#             sum2=sum2+n[i][j]
#         j=j+1
#     i=i+1
# a.append(sum)
# a.append(sum1)
# a.append(sum2)
# print(a)