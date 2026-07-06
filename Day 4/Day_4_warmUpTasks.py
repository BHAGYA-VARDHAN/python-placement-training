# # create an object
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print("Name of person: ",self.name)
#         print("Age of person",self.age)

# person1 = Person("Alice",30)
        
# # Define methods:
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         # print("Name of person: ",self.name)
#         # print("Age of person",self.age)
#     def introduce(self):
#         print(f"Hello, Good Morning. \n I am {self.name}, I am {self.age} yrs old")

# person1 = Person("Alice",30)
# person1.introduce()
        
        
# #Method overriding
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print("Name of person: ",self.name)
#         print("Age of person",self.age)
#     def introduce(self):
#         print(f"Hello, Good Morning. \n I am {self.name}, I am {self.age} yrs old")

# class Student(Person):
#     def __init__(self, name, age, id):
#         self.id = id
#         super().__init__(name, age)
    
#     def introduce(self):
#         super().introduce()
#         print(f" and my student id is {self.id}")        
        
# student1 = Student('Alice',21,1001)
# student1.introduce()


# #Static Methods:
# class Student():
#     def __init__(self, name, age, id):
#         self.id = id
        
#     def introduce(self):
#         super().introduce()
#         print(f" and my student id is {self.id}")     
    
#     @staticmethod
#     def validate_student_id(id):
#         if id == "12345":
#             print(True)
#         else:
#             print(False)
# Student.validate_student_id("123456")  


# for i in range(1,11):
#     print(f"{2*i} {3*i} {4*i} {5*i} {6*i} {7*i} {8*i} {9*i} {10*i}")
# print("-"*30)
# for i in range(1,11):
#     print(f"{11*i} {12*i} {13*i} {14*i} {15*i} {16*i} {17*i} {18*i} {19*i} {20*i}")


# count = 0
# for i in range(9):
#     if i %2 ==0:
#         print(i,end=" ")
#     else:
#         print(i)
#         count +=1
        
# print("count = ",count)


# # WAP to accept any one day and check it is weekend or working day
# day = input("Enter day :").lower()
# if day == "saturday" or day == "sunday":
#     print("Weekend :",day)
# else:
#     print("Working day: ",day.upper())


# #REVERSE NUMBER WITHOUT LOOP  
# num = 123
# a = num % 10
# num = num //10
# b = num % 10
# c = num //10

# rev = a*100+b*10+c*1
# print("reverse : ",rev)

# num = 1234567
# a = num % 10
# num = num //10

# b = num % 10
# num = num //10

# c = num % 10
# num = num //10

# d = num % 10
# num = num //10

# e = num % 10
# num = num //10

# f = num % 10

# num = num //10

# g = num % 10 

# rev = (a*1000000) + (b*100000)+ (c*10000) + (d*1000) + (e*100) +( f*10 )+ (g*1)

# print(rev)


# #WAP for change calculation wrt Total amount

# amount = int(input("Enter amount: "))
# print("100 Rupees : ",amount // 100)
# print("50 Rupees : ",(amount % 100)//50)
# print("20 Rupees : ",((amount % 100) % 50)//20)
# print("10 Rupees : ",(((amount % 100) % 50) % 20)//10)
# print("5 Rupees : ",((((amount % 100) % 50) % 20) % 10) // 5)
# print("2 Rupees : ",(((((amount % 100) % 50) % 20) % 10)% 5) // 2)
# print("1 Rupees : ",((((((amount % 100) % 50) % 20) % 10)%5 ) % 2) // 1)


# #WAP to accept 3 ages and check the max age and print
# age1 = int(input("enter age 1: "))
# age2 = int(input("enter age 2: "))
# age3 = int(input("enter age 3: "))

# if age1 > age2:
#     if age1 > age3:
#         print(age1)
#     else:
#         print(age3)
# else:
#     if age2 > age3:
#         print(age2)
#     else:
#         print(age3)


# #WAP to accept any 1 character and check the entered character is uppercase, lowercase, digit, special symbol
# #print msg wrt to the enterred characters

# char = input("Enter any single character")
# code = ord(char) # converts keyboard character to ASCII code
# print(code)
# if  code >=65 and code <= 90:
#     print("UPPER CASE")

# elif code >=97 and code <=122:
#     print("lower case")

# elif code >= 48 and code <=57:
#     print("Digit")

# elif code == 32:
#     print("Space")

# elif code == 10:
#     print("New line")
    
# else:
#     print("Special Character")

# if-else : accept until valid credential
# while True:
#     username = input("Enter Username :")
#     password = input("Password: ")
#     if username == password:
#         print("Login Successfull")
#         break
#     else:
#         print("Invalid Credential..")
#         print("Try again...")
#         print("-"*30)

# # STRING FUNCTIONS
# s = "help4code is best platform for practicing programming"
# print(s.find("help4code"))
# print(s.find("python"))
# print(s.find("programming")) # find() => starting index of number of string if it is found else returns -1


# s = "prashant","ashish","sandip"
# m = '|'.join(s) #join() => replaces the character that seperates two strings and returns new updated string
# print(m) # prashant|ashish|sandip

# s = "Python is a High level programming Language"
# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# print("Subject Marks: ")
# phy = 50 
# chem = 60 
# math = 70

# print("Physics = {} Chemistry = {} Math = {}".format(phy,chem,math))
# print("Physics = {0} Chemistry = {1} Math = {2}".format(phy,chem,math))
# print("Physics = {x} Chemistry = {y} Math = {z}".format(x = phy,y = chem,z = math))

# total = phy+chem+math
# print(f"Total marks :{total}")
# print("Roll Number=","25".zfill(4))


# # TRAVERSING A STRING
# name = "help4code"
# for i in name:
#     print(i)


# name = "prashant"
# i = 0
# for x in name :
#     if x == 'n':
#         print("The character present at index number ",i," value := ",x)
#         break
#     i+=1



# a = 'shiwaleew'
# for i in a:
#     if i == 'w':
#         print(i)



# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]

# print(id(x))
# print(id(y))
# print(id(z))

# print(x==y)
# print(x==z)
# print(x!=z)



# a = 50
# b = 30
# c = 20
# d = 10

# print((a+b)*c/d) # 80*2 -> 160
# print((a-b)*(c/d)) # 20*2
# print(a+(b*c)/d) # 50+600/2


# Removing spaces from the string:
#1. rstrip() -> To remove spaces at right hand side
#2. lstrip() -> To remove spaces at left hand side
#3. strip() -> To remove spaces of both side

# city = input("Enter City name: ")
# scity = city.strip().title()
# if scity =="Hydrabad":
#     print("Hello Hydrabadi...ADAB")
    
# elif scity == "Chennai":
#     print("Hello Madrasi...VANAKKAM")

# elif scity == "Banglore":
#     print("Hello Kannadiga...SHUBHODAYA")

# else:
#     print("RAM RAM MANDALI...")


# #replacing a string with another string
# s = ""
# s1 = s.replace("difficult","easy")
# print(s1)

# s = 'ababababababababab'
# s1 = s.replace('a','b')
# print(s1)

# '''
# ip = 'gasgg54@#vscsd!s*
# op = 4
# '''

# ipStr = input("Enter string of special character ")
# count = 0
# for i in ipStr:
#     if i.isalpha() or i.isnumeric():
#         pass
#     else:
#         count+=1
# print("Special Characters: ",count)