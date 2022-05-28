# grocery_list=["flour","cheese","carrots"]
# i=0
# while i<len(grocery_list):
#     print(i,":",grocery_list[i])
#     i=i+1

# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j=j+1
#     i=i+1
# b="".join(b)
# print(b)

# List product excluding duplicates.
# List = [6,1,3,5,6,3,1]
# Output: 60
# list=[6,1,3,5,6,3,1]
# i=0
# b=[]
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#     i=i+1
# print(b)
# p=1
# i=0
# c=[]
# while i<len(b):
#     p=p*b[i]
#     i=i+1
# print(p)

# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.

# a=[1,2,2,5,8,4,4,8]
# i=0
# b=[]
# count=0
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#         count=count+1
#     i=i+1
# print(b)
# print(count)

# Find the First Maximum, Second maximum, Third maximum number from the List.

# a=[1,2,3,45,8]
# i=0
# max=0
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# print(max)
# i=0
# second_max=0
# while i<len(a):
#     if a[i]>second_max and a[i]!=max:
#         second_max=a[i]
#     i=i+1
# print(second_max)
# i=0
# third_max=0
# while i<len(a):
#     if a[i]>third_max and a[i]!=max and a[i]!=second_max:
#         third_max=a[i]
#     i=i+1
# print(third_max)
# print("first_max",max)
# print("second_max",second_max)
# print("third_max",third_max)


# For example, if we give 9119 the function should return 811181, as the square of 9 is 81 and square
# of 1 is 1.
# n=int(input("how many elements you want in your list?"))
# i=0
# b=[]
# while i<n:
#     a=int(input("enter the number"))
#     b.append(a)
#     i=i+1
# print(b)
# i=0
# while i<len(b):
#     print(b[i]**2,end="")
#     i=i+1

# 12. You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'

# a=int(input("enter the number"))
# b=len(str(a))
# i=b-1
# while i>=0:
#     c=a//(10**i)
#     d=c*(10**i)
#     a=a%(10**i)
#     i=i-1
#     print(d,"+",end="")

# 15. Write a Python program to scramble the letters of string in a given list.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tl is', 'ecrsseiex', 'ccpitear', 'noiltuos']

# l=["python","list","exercise","practice","solution"]
# i=0
# l1=[]
# while i<len(l):
#     a=l[i][::-1]
#     i=i+1
#     l1.append(a)
# print(l1)

# l=["python","list","exercise","practice","solution"]
# i=0
# b=[]
# while i<len(l):
#     a=l[i][::-1]
#     b.append(a)
#     i=i+1
# print(b)

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

from ctypes import LittleEndianStructure


# n=[1,2,3,4,5,6,7,8,9,10]
# i=0
# a=[]
# while i<len(n)-1:
#     a.append(n[i+1]-n[i])
#     i=i+1
# print(a)


# n=[2,4,6,8]
# i=0
# a=[]
# while i<len(n)-1:
#     a.append(n[i+1]-n[i])
#     i=i+1
# print(a)


# 24. Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

# list=[1,2,3,1,2,2]
# i=0
# b=[]
# while i<len(list):
#     if list[i] not in b:
#         b.append(list[i])
#     i=i+1
# print(b)


# 25. Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2

# a=[4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
# k=3
# i=0
# b=[]
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


# a=[4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# b=[]
# k=2
# i=0
# while i<len(a):
#     n=a[i]
#     j=0
#     c=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c=c+1
#         j=j+1
#     if c>=k:
#         if n not in b:
#             b.append(n)
#         i=i+1
#     print(b)


# 50. Write a Python program to join two given list of lists of same length, element wise.
# Original lists:
# [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# [[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# Join the said two lists element wise:
# [[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]
# Original lists:
# [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# Join the said two lists element wise:
# [['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

# a=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]
# b=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
# i=0
# c=[]
# while i<len(a):
#     c.append(a[i]+b[i])
#     i=i+1
# print(c)

# a=[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
# b=[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]
# c=[]
# i=0
# while i<len(a):
#     c.append(a[i]+b[i])
#     i=i+1
# print(c)

# 49.
# Write a Python program to find the last occurrence of a specified item in a given list.
# Original list:
# ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# Last occurrence of f in the said list:
# 7
# Last occurrence of c in the said list:
# 15
# Last occurrence of k in the said list:
# 14
# Last occurrence of w in the said list:
# 12

# l=['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']
# i=0
# while i<len(l):
#     if l[i]=="f":
#         a=i
#     elif l[i]=="c":
#         b=i
#     elif l[i]=="k":
#         c=i
#     elif l[i]=="w":
#         d=i
#     i=i+1
# print(a,b,c,d)

# 48. Write a Python program to split a given list into specified sized chunks.
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the said list into equal size 3
# [[12, 45, 23], [67, 78, 90], [45, 32, 100], [76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the said list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]

# l=[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
# b=[]
# i=0
# while i<=len(l)-3:
#     b.append(l[i:i+3])
#     i=i+3
# print(b)

# a=[["g","f","g"],["i","s"],["b","e","s","t"]]
# i=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         b.append(a[i][j])
#         j=j+1
#     i=i+1
# b="".join(b)
# print(b)




