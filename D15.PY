# 15. Write a Python program to scramble the letters of string in a given list.
# Original list:
# ['Python', 'list', 'exercises', 'practice', 'solution']
# After scrambling the letters of the strings of the said list:
# ['tnPhyo', 'tl is', 'ecrsseiex', 'ccpitear', 'noiltuos']


l=["python","list","exercise","practice","solution"]
i=0
l1=[]
while i<len(l):
    a=l[i][::-1]
    i=i+1
    l1.append(a)
print(l1)