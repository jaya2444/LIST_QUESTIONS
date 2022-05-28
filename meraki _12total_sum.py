# Q: How to find all pairs in an array of integers whose sum is equal to the given number?
# number = 30
# n = [10, 11, 12, 13, 14, 17, 18, 19]
# Output:-
# [[11,19], [12,18],[13,17]]


# number=30
# n=[10,11,12,13,14,17,18,19]
# a=[]
# i=0
# while i<len(n):
#     j=i+1
#     while j<len(n):
#         b=n[i]+n[j]
#         if number==b:
#             sum=[n[i],n[j]]
#             a.append(sum)
#         j=j+1
#     i=i+1
# print(a)


# number=30
# n=[10,11,12,13,14,17,18,19]
# i=0
# while i<len(n)/2:
#     j=0
#     while j<len(n):
#         if n[i]+n[j]==number:
#             print([n[i],n[j]],end=" ")
#         j=j+1
#     i=i+1


        