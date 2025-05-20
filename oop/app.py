# class Student:
#     name="Sidra"

# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)

# class Car:
#     color = "blue"
#     model = "bmw"

# c1 = Car()
# print(c1.color)
# print(c1.model)

class Student:
    student_name="Sidra" #class attribute
    def __init__(self, name, age, marks):
        self.name = name  #object attribute
        self.age = age
        self.marks = marks
        print("Object Created")


    def welcome(self):
            print("Welcome to the class" , self.name)
    def get_marks(self):
        return self.age 

    def average(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("h1" , self.name , "Average is" , sum/3)          
s1 = Student("Sidra", 20 , [10,20,30])
s1.name = "Sadia"
print(s1.name)
print(s1.age)
s1.welcome() 
print(s1.get_marks())
s1.average()     