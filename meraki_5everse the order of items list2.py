# Write a code that the reverses the order of the items means in opposite order.
# Code Example

# places=["delhi", "gujrat", "rajasthan", "punjab", "kerala"]

# Your code output should be here :

# kerela
# punjab
# rajasthan
# gujrat
# delhi

place=["delhi","gujarat","rajastan","panjab","kerala"]
i=len(place)-1
while i>=0:
    print(place[i])
    i=i-1