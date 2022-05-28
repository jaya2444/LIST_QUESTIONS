# 32. Given start and end of a range, write a Python program to print all positive numbers in given range.
# Example:
# Input: start = -4, end = 5
# Output: 0, 1, 2, 3, 4, 5
# Input: start = -3, end = 4
# Output: 0, 1, 2, 3, 4

a=int(input("enter the start number"))
b=int(input("enter the  end number"))
for i in range(a,b+1):
    if i>=0:
        print(i,end=",")
    i=i+1


# for i in range(-4,6):
#     if i>=0:
#         print(i,end=",")

# for i in range(-3,4):
#     if i>=0:
#         print(i,end=",")

