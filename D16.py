# 16. W rite a Python program to find the difference between elements (n+1th - nth) of a given list of numeric
# values.
# Original list:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Difference between elements (n+1th - nth) of the said list :
# [1, 1, 1, 1, 1, 1, 1, 1, 1]
# Original list:
# [2, 4, 6, 8]
# Difference between elements (n+1th - nth) of the said list :
# [2, 2, 2]


n=[1,2,3,4,5,6,7,8,9,10]
i=0
a=[]
while i<len(n)-1:
    a.append(n[i+1]-n[i])
    i=i+1
print(a)



# n=[2,4,6,8]
# i=0
# a=[]
# while i<len(n)-1:
#     a.append(n[i+1]-n[i])
#     i=i+1
# print(a)



