# Defining Lists-
# To define lists we can use square brackets - [].
# Whenever you see [, then think that list definition has started, and when you see ], then think that list definition is ending.
# Some Examples-
# In this example, we will store the names of students in a list.
# names_list = ["rahul", "shivam", "kavay", "ashish", "rohit"]
# print(names_list)
# print(type(names_list))
# In the last line we have used type. By using this function we will come to know that what is its data type.
# This is the list of strings because all of its values contain strings.

# We can put any object inside a list. This can be string, integer or any other data type.
# if we will use type function on a list variable, it will always show the type as list.But we the data iside a list can be of any type.

# MIXED LISTS-
# Its not like that lists should have same type of data. Data inside list can be of any type.
# Example:-
# mixed_list = ["rahul", 12, 9.0, "kaavay", "shivam", 1]
# print(type(mixed_list))
# But, this is not a very common practice. Usually we keep same type of Data in a list


# A list contains a collection of values. So we need to find a way, that how can we access these values.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(names_list[1])
# when we wrote nameslist[1]? Did "shivam" got printed? yes shivam printed.

# Here, [1] is called INDEX. To access any item of a list, we use the INDEX of that item. 
# Let us see what is the index of all the items in the given list.

# ["annu", "shivam", "deepa", "pooja", "rupa"]
# 1.annu has index 0
# 2.shivam has index 1
# 3.deepa has index 2
# 4.pooja has index 3
# 5.rupa has index 4
# If we see carefully, then we will notice that the INDEX of that ITEM is one less than its position. The counting of the INDEX starts from 0, not from 1.
 
#  ["annu","shivam","deepa","pooja","rupa"]
#   0	        1	   2	   3	   4

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]

# print(names_list[0]) # se "annu" print hoga

# print(names_list[4]) # se "rupa" print hoga

# print(names_list[5]) # index out of range
# the last line gives us error.
# Simply means - whatever INDEX you have given, that INDEX is out of range of the given indices of list. (indices - plural of index).


# Question-

# What is the maximum INDEX that we can put?
# Answer-

# 1 less than the length of the INDEX. If we will put more value than the range of the index, then index out of range error will come.


# Changing List Items-

# In the same way we can update/change the ITEMS in a given LIST.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list[0] = "abhishek"
# print(names_list)
# op=["abhishek", "shivam", "deepa", "pooja", "rupa"]

# The ITEM present at 0 INDEX has now been changed to "abhishek". Similarly,

# names_list = ["abhishek", "shivam", "deepa", "pooja", "rupa"]
# names_list[3]="rishabh"
# print(names_list)
# op=["abhishek", "shivam", "deepa", "rishabh", "rupa"]

# The ITEM that was present at INDEX 3 has now changed to "rishabh". Keep in mind that INDEX is 1 less than the position of the item. Similarly, if you write something as given below :

# names_list = ["abhishek", "shivam", "deepa", "rishabh", "rupa"]
# names_list[5]="dhruv"
# print(names_list)
# So, we will get a list index out of range error, because at the 5th index no item exists. 

# Length of List and Adding values of the List-
# If we want to see the length of the list then we use the len () (length function).
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(len(names_list))

# If we want to add one new value to a list then we will use append function. By using the append(), we can add an element at the end of the list.
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# print(names_list)
# names_list.append("dhruv")
# print("length of the list is ", len(names_list))
# print(names_list)
# Here, you can see that previously the list length was 5 but after using the append(), the length of the list became 6. When you printed names_list then the value dhruv was added in the last.

# Let's append once again.

# names_list = ["annu", "shivam", "deepa", "pooja", "rupa"]
# names_list.append("alok")
# print("length of the list is ", len(names_list))
# print(names_list)
# In this way, you can add as many elements as you want.

# Removing Elements from a List-
# Just as we can add elements to the list, similarly we can remove elements from the list we can use the pop(). To remove the last element from the list we can use the pop function.
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# names_list.pop()
# print("length of the list is ", len(names_list))
# print(names_list)
# we can use pop function with an argument also on a given list. That means you can also add index to the pop function, which will remove the desired element of the given index from the list. 
# Example :-
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print("length of the list is ", len(names_list), names_list)
# names_list.pop(2)
# print("length of the list is ", len(names_list), names_list)



# Check if Element exists in List-

# We can do a lot of interesting operations on the list. One of the important operations of lists is to check whether a particular element is present in the given ITEM LIST or not.
# Example:-
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("shivam" in names_list)
# Its result will come as True because "shivam" element exists in names_list.
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# print("imtiyaz" in names_list)
# Its result will come as False because "imtiyaz" element does not exist in the names_list.
# As this is a Boolean value, it will return (True/False), we can also use it with the if statement.
# Example :-
# names_list = ["annu", "shivam", "deepa", "pooja", "rupa", "dhruv", "alok"]
# if "shivam" in names_list:
#  print("Shivam ka naam names_list mei hai")
# else:
#  print("Shivam ka naam names_list mei nahi hai.")

# ITERATION-
# In a class, the teacher marks attendance by calling out their names one by one, from a list of students. This process is called Iteration.
# ITERATE MEAN-bar bar dohrana,punravratti
# Basically, the work that we do repeatedly is called as Iteration.




# Using loops, we have learned how to do iteration. But , we don't know how to iterate over a list. Now we will learn how to run loop on any list.

# In this example, we will understand that how to iterate over the list.
# Please we see the example given below:-

# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]


# In this list all the elements have specific index.

# "robin" - 0

# "anamika" - 1

# "faisal" - 2

# "valmiki" - 3

# "waseem" - 4

# "amara" - 5

# Now, we will use while loop, increase the counter one by one and we can access the elements of the list one by one.
# Example :-

# students_list = ["robin", "anamika", "faisal", "valmiki", "waseem", "amara"]
# list_length = len(students_list)
# index = 0
# while index < list_length:
#     print(students_list[index])
#     index = index + 1
# Here we have to check in the while loop that the value of the index should be less than the list_length. The loop will stop working at the moment when the index value will become equal to the list_length.

# One More Example-
# To calculate the total marks of a student from the student's marks list we will use the following code.
# student_marks = [23, 45, 89, 90, 56, 80] 
# length = len(student_marks)
# index = 0
# total_marks = 0
# while index < len(student_marks):
#     total_marks = student_marks[index] + total_marks
#     index = index + 1
# print("Total Marks: " + str(total_marks))

# sum of the list-
# a=[2,4,1,3,3]
# i=0
# sum=0
# while i<len(a):
#     sum=sum+a[i]
#     i=i+1
# print(sum)
# op=13

# One Final Example-

# Suppose we have a list of marks and we have to find that how many students have marks less than 50. For doing this we write the code given below.

# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# list_length = len(student_marks)
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < list_length:
#     marks = student_marks[index]
#     if marks < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print("Marks more than 50: " + str(more_than50))
# print("Marks less than 50: " + str(less_than50))


# student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
# index = 0
# less_than50 = 0
# more_than50 = 0
# while index < len(student_marks):
#     if student_marks[index] < 50:
#         less_than50 = less_than50 + 1
#     else:
#         more_than50 = more_than50 + 1
#     index = index + 1
# print("Marks more than 50:",more_than50)
# print("Marks less than 50:",less_than50)



