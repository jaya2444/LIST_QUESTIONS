# 47. Write a Python program to convert a given list of strings into list of lists.
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]

l=["red","maroon","yellow","olive"]
a=[]
i=0
while i<len(l):
    a.append(list(l[i]))
    i=i+1
print(a)

# l=["red","maroon","yellow","olive"]
# b=[]
# for i in l:
#     b.append([j for j in i])
# print(b)
