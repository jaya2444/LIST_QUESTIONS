# 38. Write a Python program to check if a given string contains an element, which is
# present in a list.
# The original string and list:
# https://www.w3resource.com/python-exercises/list/
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.com/python-exercises/list/ contains an element, which
# is present in the list ['.com', '.edu', '.tv']
# True
# The original string and list: https://www.w3resource.net
# https://www.w3resource.net
# ['.com', '.edu', '.tv']
# Check if https://www.w3resource.net contains an element, which is present in the list
# ['.com', '.edu', '.tv']
# False


m="https://www.w3resource.com/python-exercises/list/"
l=[".com",".edu",".tv","https"]
i=0
while i<len(l):
    if l[i] in m:
        print("true")
        break
    else:
        print("false")
        break
    i=i+1
