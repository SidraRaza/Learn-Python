name = "hello" + " " + "world"
print(name)

# escape sequence character

space = "hello \nworld"
print(space)


name2= len(name)
print(name2)

# indexing

name3 = "hello world"
print(name3[0])

# string slicing

name4 = "hello world"
print(name4[1:4])
print(name4[5:])
print(name4[-3:-1])
  

#string Functions  
str="i am studying python from GIAIC" 
print(str.endswith("AIC"))
print(str.endswith("python"))
print(str.capitalize())
print(str.replace("o","e"))
print(str.replace("GIAIC","GIA"))
print(str.find("o"))
print(str.find("python"))
print(str.count("o"))

name5= input("enter your first name : ")
print(len(name5))


occurence = "I am a  $ student of GIAIC $"
print(occurence.count("$"))