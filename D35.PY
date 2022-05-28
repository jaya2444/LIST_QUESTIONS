# 35. Write a Python program to check if first digit/character of each element in a given list
# is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if the first digit in each element of the given list is the same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False


list=[1234,133,1984,19372,123]
i=0
b=str(list[0])[0]
count=0
while i<len(list):
    a=str(list[i])
    if a[0]==b:
        count=count+1
    i=i+1
if count==len(list):
    print("True")
else:
    print("False")
    


