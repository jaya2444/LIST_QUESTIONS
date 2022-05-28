# 31. Given the start and end of a range, write a Python program to print all negative numbers in a given
# range.
# Example:
# Input: start = -4, end = 5
# Output: -4, -3, -2, -1
# Input: start = -3, end = 4
# Output: -3, -2, -1


a=int(input("enter the start number"))
b=int(input("enter the  end number"))
for i in range(a,b+1):
    if i<0:
        print(i,end=",")
    i=i+1


# for i in range(-4,5):
#     if i<0:
#         print(i,end=",")

# for i in range(-3,4):
#     if i<0:
#         print(i,end=",")