print("it is your question")
qu=[
    ["which is the capital of India?"],
    ["who is the prime minister of India?"],
    ["which course teach in Navgurukul?"],
    ["who is the father of India?"]
]
op=[
    ["Goa","Karnatak","Kerla","New Delhi"],
    ["Rajnath Kovind","Jawaharlal Nehru","Narendra Modi","Atul Bihari Vajpei"],
    ["Software engineering","Agriculture","Science and Technology","Medical course"],
    ["Mahatma Gandhi","Rajnath Kovind","Atul Bihari Vajpei","Apj Abdul Kalam"]
]
option50_50=[
    ["1)Goa","4)New Delhi"],
    ["2)Jawaharlal Nehru","3)Narendra Modi"],
    ["1)Software enginerering","3)Science and Technology"],
    ["1)Mmahatma Gandhi","2)Apj Abdul Kalam"],
]
ans_list=[4,3,1,1] 
i=0
count=0
price=0
while i<len(qu) :
    print(qu[i])
    j=i
    sno=0
    while (sno<len(op[i])):
        a=op[j][sno]
        print(sno+1,a)
        sno=sno+1
    lifeline=input("do u want lifeline?yes/no")
    if lifeline=="yes":
        print("select your option")
        if count<1:
            se=0
            b=i
            while se<len(option50_50[i]):
                c=option50_50[b][se]
                se=se+1
                print(c)
            ans=int(input("choose your answer"))
            if ans==ans_list[i]:
                price=price+1000
                print("your answer is correct,and your winning is",price)
                print("congratulations")
                print("your next question is")
            else:
                print("your answer is wrong")
                print("your next quesstion is")
            count=count+1
        else:
            print("you already use ur lifeline")
            ans1=int(input("plz enter your answer"))
            if ans1==ans_list[i]:
                price=price+1000
                print("your answer is correct,and your winning price",price)
                print("congratulations")
            else:
                print("your answer is wrong")
                print("your next question is")
                break
    else:
        ans2=int(input("enter your number"))
        if ans2==ans_list[i]:
            price=price+1000
            print("your answer is correct and your winning price is",price)
        else:
            print("wrong number")
    i=i+1

    





question_list=[
    ["which is the capital of India?"],
    ["who is the prime minister of India?"],
    ["which course teach in Navgurukul?"],
    ["who is the father of India?"]
]
option=[
    ["Goa","Karnataka","Kerala","New Delhi"],
    ["Rajnath Kovind","Javaharlal Nehru","Narendra Modi","Atul Bihari Vajpei"],
    ["Software Engineering","Agriculture","Science and Technologyg","Medical coures"],
    ["Mahatma Gandhi","Rajnath Kovind","Atul Bihari Vajpei","APJ Abdul Kalam"],
]
option50_50=[
    ["1)Goa","4)New Delhi"],
    ["2)Jawaharlal Nehru","3)Narendra Modi"],
    ["1)Software Engineering","3)Science and Techonology"],
    ["1)Mahatma Gandhi","2)APJ Abdul Kalam"],
    ["1)Mahatma Gandhi","2)APJ Abdul Kalam"],
]
ans_list=[4,3,1,1]
print("kon banega karodpati,kbc")
print("lets start the game")
i=0
c=0
s=10000
while i<len(question_list):
    print(question_list[i])
    a=0
    while a<len(option[i]):
        k=option[i][a]
        print(a+1,k)
        a=a+1
    if c==0:
        life_line=input("do you want to use lifeline n/y:-")
        if life_line=="yes":
            c=c+1
            print(option50_50[i])
    answer=int(input("enter the option"))
    if ans_list[i]==answer:
        print("your answer is correct",s)
        s=s+10000
    else:
        print("your answer is wrong")
        break