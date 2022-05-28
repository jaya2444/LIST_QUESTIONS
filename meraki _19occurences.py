# Count Occurences-
# Occurences - is made from the word occur which means that how many times a certain character or word appears.
# Sample List-
# char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
# Output of the Sample List-
# [["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]]
# a - 6 times
# n - 3 times
# t - 2 times
# x - 2 times
# u - 1 times
# g - 1 times
# We have to count the occurences of characters present in the char_list and we have to save in the nested list, then we have to use that nested list to print the output.




a = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c=0
c1=0
c2=0
c3=0
c4=0
c5=0
while i<len(a):
    if "a" in a[i]:
        c=c+1
    elif "n" in a[i]:
        c1=c1+1
    elif "t" in  a[i]:
        c2=c2+1
    elif "x" in a[i]:
        c3=c3+1
    elif "u" in a[i]:
        c4=c4+1
    else:
        c5=c5+1
    i=i+1
print("a-",c,"times")
print("n-",c1,"times")
print("t-",c2,"times")
print("x-",c3,"times")
print("u-",c4,"times")
print("g-",c5,"times")
print([["a",c],["n",c1],["t",c1],["x",c2],["u",c3],["g",c5]])





