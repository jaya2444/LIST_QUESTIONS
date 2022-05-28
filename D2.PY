# 2. Convert Character Matrix to single String;
# The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest


list= [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
b=[]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        b.append(list[i][j])
        j+=1
    i+=1
b="".join(b)
print(b)