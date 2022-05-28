# count-elements

# Write a program that tells how many elements are there in a given list. It is similar to len() function, so in order to implement this program we will not use len() function but we will try to understand that how did any programmer implemented this len() function.
# Code Example

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]



# l=[1,2,3,4,5,6,45,87]
# count=0
# for x in l:
#     count=count+1
# print("length of list",count)

l=[50, 40, 23, 70, 56, 12, 5, 10, 7]
count=0
i=0
while i<len(l):
    count=count+1
    i=i+1
print("length of list",count)

