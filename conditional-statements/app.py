age = 21

if(age>=18):
    print("You can vote")
elif(age<18):
        print("You can't vote")
else:
        print("Invalid age")

student_list = ["tuesday", "friday", "saturday", "sunday"]

if "tuesday" in student_list:
    print("I am a student of Tuesday class") 
elif "wednesday" in student_list:
    print("I am a student of Wednesday class")
else:
    print("I am a student of Thursday class")


students = ["Sidra", "Ahmed", "Iqra", "Danish", "Asad"] 

if len(students) == 4:
    print("Found")
elif len(students) == 7:
    print("Found") 
else:
    print("Not found")
            

numberOfIndexing = "Sidra Raza"

if "hj" in numberOfIndexing:
    print("Raza is present in our string") 
elif "Sidra" in numberOfIndexing:
    print("Sidra is present in our string")
else:
    print("Not found")
     