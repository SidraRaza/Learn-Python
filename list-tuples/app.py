marks = [34.6,67.9,76.8,34.6,67.9,76.8]
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
mixData = ["iqra","iqu","Ahmed",34,76.8]
mixData[1]="sidra"
print(mixData)
check_len=len(mixData)
print(check_len)
print(mixData[1:4])


listInInput=list(input("Enter Your Data: "))
print("List Data :", listInInput)

num1=[3,8,9,5,6]
# add item in list 
num1.append(1)
# remove item in list
num1.remove(3)
# sort item in list
num1.sort()
# sort reverse item in list
num1.sort(reverse=True)
# reverse item in list 
num1.reverse()
# insert item in list
num1.insert(1,4)
print(num1)

# Tuple

tup= (1,2,3,4,5)
print(type(tup))
# indexing in tuple
print(tup[0])


# TypeError: 'tuple' object does not support item assignment
# tup[0]=4
# print(tup)

tup1=()
print(type(tup1))
print(tup1)

tup2 = (1,)
print(type(tup2))
print(tup2)

tup3_int = (1)
print(type(tup3_int))
print(tup3_int)

tup_float = (1.5)
print(type(tup_float))
print(tup_float)

tup_string = ("iqra")
print(type(tup_string))
print(tup_string)

# slicing in tuple
sliceing=(1,2,3,4,5)
print(sliceing[0:3])
 
# index in tuple
index=(1,2,3,4,5)
print(index.index(3))

# count in tuple
count=(1,2,3,4,5,1)
print(count.count(1))

# practice questions
movies=[]
movie1=input("Enter Your Favorite Movie Name1: ")
movie2=input("Enter Your Favorite Movie Name2: ")
movie3=input("Enter Your Favorite Movie Name3: ")
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

# check palindrome of element in list
myList=["iqra","sidra","iqra"]
myList1=myList.copy()
myList1.reverse()
if(myList==myList1):
    print("palindrome")
else:
    print("not palindrome")

# count method in tuple
tup=("C","D","A","A","B","B","A")
print(tup.count("A"))

# sort method in tuple
sort_tuple=("C","D","A","A","B","B","A")
print(sorted(sort_tuple))

