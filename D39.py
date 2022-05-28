# 39.
# Write a Python program to compute the average of n th elements in a given list of
# lists with different lengths.
# Original list:
# [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
# Average of n-th elements in the said list of lists with different lengths:
# [4.8, 5.8, 6.8, 8.0, 11.0]



n=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
sum=0
sum1=0
sum2=0
sum3=0
sum4=0
c=0
c1=0
c2=0
c3=0
c4=0
a=[]
while i<len(n):
    j=0
    while j<len(n[i]):
        if j==0:
            sum=sum+n[i][j]
            c=c+1
        elif j==1:
            sum1=sum1+n[i][j]
            c1=c1+1
        elif j==2:
            sum2=sum2+n[i][j]
            c2=c2+1
        elif j==3:
            sum3=sum3+n[i][j]
            c3=c3+1
        else:
            sum4=sum4+n[i][j]
            c4=c4+1
        j=j+1
    i=i+1
a.append(sum/c)
a.append(sum1/c1)
a.append(sum2/c2)
a.append(sum3/c3)
a.append(sum4/c4)
print(a)
