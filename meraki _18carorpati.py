# How many Crorepati?
# Code Example

# kitna_paisa_hai = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]

# Write a program that tells in the above list that how many people are there in the above list who are :

# 1 - `Crorepati`
# 2 - `Lakhpati`
# 3 - `Dilwale`

# All those who have money more than or equal to 1 crore are known as Crorepati. All those who have money money greater than or equal to 1 lakh, those are called Lakhpati. Rest of the people are called Dilwale.

# For example, the output of the list given above is as follows.

# 4 Crorepati
# 3 Lakhpati
# 4 Dilwale



n = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
c=0
c1=0
c2=0
while i<len(n):
    if n[i]>=10000000:
        c=c+1
    elif n[i]>=100000:
        c1=c1+1
    else:
        c2=c2+1
    i=i+1
print("caroepati",c)
print("lakhpsti",c1)
print("dilwale",c2)