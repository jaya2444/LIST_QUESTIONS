# Write a code, that counts the numbers between 20 and 40 and then print its count.

# numbers=[50, 40, 23, 70, 56, 12, 5, 10, 7]


l=[50,40,23,70,56,18,5,10,7]
i=0
count=0
while i<len(l):
    if l[i]>20 and l[i]<40:
        count=count+1
    i+=1
print(count)