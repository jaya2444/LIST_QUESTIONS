# 26. Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22



# n=[4,5,5,5,3,8]
# i=0
# while i<len(n)-1:
#     if n[i]==n[i+1] and n[i+1]==n[i+2]:
#         print(n[i])
#     i=i+1

n=[1,1,1,64,23,64,22,22,22]
i=0
a=[]
while i<len(n)-2:
    if n[i]==n[i+1] and n[i+1]==n[i+2]:
        a.append(n[i])
    i=i+1
print(a)


# n=[1,1,1,64,23,64,22,22,22]
# i=0
# while i<len(n)-2:
#     if n[i]==n[i+1] and n[i+1]==n[i+2]:
#         print(n[i],end=" ")
#     i=i+1