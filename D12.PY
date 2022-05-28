# 12. You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12 # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304 # Should return '70000 + 300 + 4'


# string=input("enter the number")
# add=""
# i=0
# while i<len(string):
#     add=add+string[i]
#     j=1
#     while j<=(len(string)-(i+1)):
#         add=add+"0"
#         j=j+1
#     if i==(len(string)-1):
#         pass
#     else:
#         add=add+"+"
#     i=i+1
# print(add)



# a=input("enter the number")
# l=len(a)
# i=l-1
# b=[]
# c=int(a)
# while i>=0:
#     rev=c//(10**i)
#     sum=rev*(10**i)
#     c=c%(10**i)
#     i=i-1
#     b.append(sum)
# print(b)


# a=int(input("enter the number"))
# b=len(str(a))
# i=b-1
# while i>=0:
#     c=a//(10**i)
#     d=c*(10**i)
#     a=a%(10**i)
#     i=i-1
#     print(d,"+",end="")



