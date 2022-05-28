# 46.
# Write a Python program to concatenate element-wise three given lists.
# Original lists:
# ['0', '1', '2', '3', '4']
# ['red', 'green', 'black', 'blue', 'white']
# ['100', '200', '300', '400', '500']
# Concatenate element-wise three said lists:
# ['0red100', '1green200', '2black300', '3blue400', '4white500']

l1=["0","1","2","3","4"]
l2=["red","green","black","blue","white"]
l3=["100","200","300","400","500"]
i=0
m=[]
while i<len(l1):
    m.append(l1[i]+l2[i]+l3[3])
    i=i+1
print(m)