# how many times we can write three digits number in different ways

# a=[1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i],a[j],a[k])

# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if (i!=j and j!=k and i!=k):
#                 print(a[i],a[j],a[k])
#             k=k+1
#         j=j+1
#     i=i+1

# num=[0,9,5]
# for i in range(3):
#     for x in range(3):
#         for z in range(3):
#             if (i!=x and x!=z and i!=x):
#                 print(num[i],num[x],num[z])

# interview questions

# name=input("enter the name")
# if name>="a" and name<="z":
#     print("string")
# else:
#     print("integer")


# how to find sum and average of list

# num=[23,14,56,12,19,9,15,25,31,42,43]
# i=0
# sum=0
# while i<len(num):
#     sum=sum+num[i]
#     i=i+1
#     avg=sum/len(num)
# print(sum)
# print(avg)


#reverse of list

# a=input("enter the number")
# i=1
# b=[]
# while i<=len(a):
#     b.append(a[-i])
#     i=i+1
# print(b)

# how to take input list from user

# size=int(input("enter the size of list"))
# i=0
# b=[]
# while i<size:
#     num=int(input("enter the number"))
#     b.append(num)
#     i=i+1
# print(b)

# reverse of list

# a=[100,200,300,400]
# i=1
# while i<=len(a):
#     print(a[-i])
#     i=i+1


# this program will tell us seperately which is vowel and consonant 

# a=input("enter the string")
# i=0
# while i<len(a):
#     if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
#         print("vowel",a[i])
#     else:
#         print("constonant",a[i])
#     i=i+1
# print(a)


# output will be=[1,11,1,111]


# a=[10,101,1900,17100]
# i=0
# d=[]
# while i<len(a):
#     b=str(a[i])
#     c=""
#     j=0
#     while j<len(b):
#         if b[j]!="0":
#             c=c+b[j]
#         j=j+1
#     d.append(int(c))
#     i=i+1
# print(d)

# this program will tell us seperately integer,string,float value from the list

# a=[1,"a",2,"b",3,"c",4]
# i=0
# b=[]
# while i<len(a):
#     if type(a[i])==int:
#         b.append(a[i])
#     i=i+1
# print(b)

# count spaces

# a="my name is jaya kumawat"
# i=0
# c=0
# while i<len(a):
#     if a[i]==" ":
#         c=c+1
#     i=i+1
# print(c)


# replace 2 and 5 from the list by 9

# a=[1,4,2,3,4,5,7,8,9,6]
# i=0
# b=[]
# k=2
# while i<len(a):
#     if i==k:
#         a.pop(2)
#         b.append(9)
#         k=k+2
#     b.append(a[i])
#     i=i+1
# print(b)


# sum and product of those numbers which are less than 5 so do their sum and which are greater than 5 so do their product


# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# sum=0
# product=1
# while i<len(a):
#     if i<5:
#         sum=sum+a[i]
#     else:
#         product=product*a[i]
#     i=i+1
# print("sum",sum)
# print("product",product)

# in this question we have to add 100 after the indexing of 2

# a=[1,2,3,4,5,6,7]
# i=0
# b=[]
# while i<len(a):
#     b.append(a[i])
#     if i==2:
#         b.append(100)
#     i=i+1
# print(b)

# op=[0,0,0,1,1,2,2]

# a=[1,1,0,1,0,1,1]
# i=0
# b=[]
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[j]==0 and j<i:
#             c=c+1
#         j=j+1
#     b.append(c)
#     i=i+1
# print(b)

# a=[4,6,2,0,2,0,4]
# l=[]
# b=[]
# for i in a:
#     if i==0:
#         l.append(i)
#     else:
#         b.append(i)
# print(b+l)

# op=[4,6,2,2,4,0,0]


# a=[5,6,7,0,7,0,8]
# l=[]
# b=[]
# i=0
# while i<len(a):
#     if a[i]==0:
#         l.append(a[i])
#     else:
#         b.append(a[i])
#     i=i+1
# print(b+l)

# op=[5,6,7,7,8,0,0]


# l=[]
# n=int(input("enter the number"))
# i=1
# while i<=n:
#     i=i+1
#     e=int(input("enter the element"))
#     l.append(e)
# print(l)

# a=[2,4,6,[5,4],[5,7]]
# i=0
# l=[]
# sum=0
# while i<len(a):
#     if type(a[i])==int:
#         l.append(a[i])
#         sum=sum+l[i]
#     i=i+1
# print(l)
# print(sum)

# op=[2,4,6]
#     12

# l=[20,10,20,30,10,40,50]
# op=[]
# for i in l:
#     if l.count(i)==1:
#         op.append(i)
# print(op)

# op=[30,40,50]


# l=[[3,4,5,6,7,8],[1,2,3,4],[3,4,5]]
# i=0
# maxl=0
# while i<len(l):
#     j=0
#     while j<len(l[i]):
#         if len(l[i])>(maxl):
#           maxl=len(l[i])
#           print(l[i])
#         j=j+1
#     i=i+1
# print(maxl)

# op=[3,4,5,6,7,8]


# l=[3,2,4,5,6,11,12,8]
# n=int(input("enter the number"))
# i=0
# c=[]
# d=[]
# while i<len(l):
#     if l[i]>n:
#         if l[i]%2==0:
#             c.append(l[i])
#         else:
#             d.append(l[i])
#     i=i+1
# print(c)
# print(d)

# op=[6,12,8]
#     [5,11]


# a=[2,4,3,2,1,4,3]
# i=0
# count=0
# l=[]
# while i<len(a):
#     if a[i]%2==0:
#         l.append(a[i])
#         count=count+1
#     i=i+1
# print(l)
# print(count)

# op=[2,4,2,4]
#    4

# a=["b","l","a","c","k"]
# i=0
# sum=""
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)

# op=black


# l=[1,2,3,4,5,6,7,8,9,10]
# i=0
# b=[]
# while i<len(l):
#     if l[i]%3==0:
#         b.append(l[i])
#     if l[i]==8 or l[i]==10:
#         b.append(l[i])
#     i=i+1
# print(b)

# op=[3,6,8,9,10]


# list=["dd30","ss40","aa60"]
# i=0
# b=[]
# while i<len(list):
#     j=0
#     c=""
#     while j<len(list[i]):
#         if list[i][j]>="0" and list[i][j]<="9":
#             c=c+list[i][j]
#         j=j+1
#     b.append(int(c))
#     i=i+1
# print(b)

# op=[30,40,60]



# name=["jaya","aarti","bulbul","anjali"]
# animal=["camel","dog","got","cat"]
# age=["1","2","3","4"]
# i=0
# b=[]
# while i<len(name):
#     b.append(name[i]+animal[i]+age[i])
#     i=i+1
# print(b)

# op=["jayacamel1","aartidog2","bulbulgot3","anjalicat4"]



# a=[5,6,7,7,6,5,3,2,2,1,1,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==3:
#         b.append(a[i])
#     i=i+1
# print(b)

# n=[5,6,7,7,6,5,3,2,2,1,1,1]
# op=[]
# for i in n:
#     if n.count(i)==1:
#         op.append(i)
# print(op)

# n=[5,6,7,7,6,5,3,2,2,1,1,1]
# op=[]
# i=0
# while i<len(n):
#     if n.count(n[i])==1:
#         op.append(n[i])
#     i=i+1
# print(op)

# op=[3]


# a=[10,20,30,40,50]
# b=[100,200,300,400,500]
# i=0
# c=1
# while i<len(a):
#     l=str(a[i])+str(b[-c])
#     i=i+1
#     c=c+1
#     print(l)
# op=10500
#    20400
#    30300
#    40200
#    50100

# a=[1,2,3,4,5,6,7,8]
# i=0
# b=[]
# while i<len(a)-1:
#     c=str(a[i])+str(a[i+1])
#     b.append(c)
#     i=i+2
# print(b,end=",")
# op=["12","34","56","78"]

 
# a=[[1,2,3],[4,5,6],[8,9,10]]
# i=0
# max=0
# b=[]
# while i<len(a):
#     j=0
#     while j<len(a[i]):
#         if a[i][j]>max:
#             max=a[i][j]
#         j=j+1
#     i=i+1
#     b.append(max)
# print(b)

# op=[3,6,10]


# a="12345678910"
# l=[]
# b=(a[2])
# c=(a[5])
# d=(a[7:11])
# l.append(int(b))
# l.append(int(c+d))
# print(l)

# op=[3,68910]


# max min then sum of them

# a=[2,3,7,8,14,1]
# i=0
# max=0
# min=a[0]
# b=[]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     elif min>a[i]:
#         min=a[i]
#     i=i+1
# print(max)
# print(min)
# print("sum of max and min",max+min)



# l=[2,5,7,6,9]       # op=[9,5,7,6,2]


# l=[2,3,4,5,6,7,5]
# n=int(input("enter the number"))
# i=0
# sum=0
# while i<len(l):
#     if l[i]>n:
#         sum=sum+l[i]
#     i=i+1
# print(sum)

# op=13

    
# n=[3,4,5,6,7]
# b=int(input("enter the number"))
# i=0
# c=[]
# while i<len(n):
#     if n[i]<=b:
#         k=b-n[i]
#         c.append(k)
#     i=i+1
# print(c)
# op=[1,0]


# a=[-1,3,-4,8,-9,6,8]
# count=0
# count1=0
# i=0
# b=[]
# c=[]
# while i<len(a):
#     if a[i]>=0:
#         l=1
#         b.append(l)
#         count=count+1
#     elif a[i]<0:
#         m=0
#         c.append(m)
#         count1=count1+1
#     i=i+1
# print(b,count)
# print(c,count1)

# a=[1,2,3,4,56,6]
# b=(a[5:]+a[:5])
# b.pop(1)
# b.append(1)
# print(b)
# op=[6,2,3,4,56,1]


# x=[10,20,30]
# y=[40,50,60]
# x[:0]=y
# print(x)
# op=[40,50,60,10,20,30]

# duplicate remove

# a=[30,15,15,45,3,1,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         b.append(a[i])
#     i=i+1
# print(b)

# whatever number is divisible by 5 so we have to append that in one list.
# a=[30,15,15,45,3,1,8]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%5==0:
#         b.append(a[i])
#     i=i+1
# print(b)


# list=[2,4,7,8,66,55]
# op=[2,4,6655]

# list=[2,4,7,8,66,55]
# i=0
# b=[]
# while i<len(list):
#     if list[i]==2 or list[i]==4:
#         b.append(list[i])
#     elif list[4]==66 or list[5]==55:
#         d=list[4]
#         c=list[5]
#         b.append(str(d)+str(c))
#         break
#     i=i+1
# print(b)


# list=[2,4,7,8,66,55]
# i=0
# b=[]
# while i<len(list):
#     if list[i]==2 or list[i]==4:
#         b.append(list[i])
#     elif list[4]==66 or list[5]==55:
#         d=list[4]
#         c=list[5]
#         l=str(d)+str(c)
#         b.append(int(l))
#         break
#     i=i+1
# print(b)

# Q.1 write a python program to sum all the items in a list?

# a=[1,2,3,4,5,6,7]
# i=0
# sum=0
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         sum=sum+a[i]
#     i=i+1
# b.append(sum)
# print(b)

# Q.2 write a python program to multiply all the items in a list?

# a=[1,2,3,4,5]
# i=0
# p=1
# b=[]
# while i<len(a):
#     if a[i] not in b:
#         p=p*a[i]
#     i=i+1
# b.append(p)
# print(b)

# Q.3 write a python program to find largest number from a list?

# a=[1,2,3,4]
# i=0
# max=0
# b=[]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# b.append(max)
# print(b)

# Q.4 write a python program to find first max and second max number from a list?


# a=[1,2,3,4]
# i=0
# max=0
# b=[]
# while i<len(a):
#     if a[i]>max:
#         max=a[i]
#     i=i+1
# b.append(max)
# print(b)
# i=0
# smax=0
# c=[]
# while i<len(a):
#     if a[i]>smax and a[i]!=max:
#         smax=a[i]
#     i=i+1
# c.append(smax)
# print(c)

# we have to print first 5 number square and last 10 number square in one list?

# a=[]
# i=1
# while i<=20:
#     a.append(i**(2))
#     i=i+1
# # print(a)
# d=(a[:5])
# e=(a[-10:])
# print(d+e)

#we have to sum if a in b also so we have to add.
 
# a=[1,2,3]
# b=[1,3,5]
# i=0
# sum=0
# while i<len(a):
#     j=0
#     while j<len(b):
#         if a[i]==b[j]:
#            sum=sum+a[i]+b[j]
#         j=j+1
#     i=i+1
# print(sum)























