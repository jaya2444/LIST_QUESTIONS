# 25. Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.


# a=[4,6,4,3,3,4,3,4,3,8]
# k=3
# b=[]
# i=0
# while i<len(a):
#     n=a[i]
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#            c=c+1
#         j=j+1
#     if c>=k:
#         if n not in b:
#             b.append(n)
#     i=i+1
# print(b)

a=[4,6,4,3,3,4,3,4,6,6]
k=2
b=[]
i=0
while i<len(a):
    n=a[i]
    j=0
    c=0
    while j<len(a):
        if a[i]==a[j]:
           c=c+1
        j=j+1
    if c>k:
        if n not in b:
            b.append(n)
    i=i+1
print(b)


    