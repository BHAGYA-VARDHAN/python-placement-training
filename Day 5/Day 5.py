#============================================== DICTIONARY ===================================================#

# mydict = {
#     101: "Bhagyavardhan",
#     102: "ritesh",
#     "103" : "rutuja",
#     "104" : "Karishma",
#     101 : "ritesh",   # it overrides the value not key
#     104 : "ritesh"
# }
# print(mydict)
# print(type(mydict))
#with the help of key we have to print value

# a = mydict[102]
# print(a)

# replace old value with new value
# mydict[102] = "peter"
# print(mydict)

#only print keys x=0,1
# for x in mydict:
#     print(x) #bydefault looping statement access the key

# only print values
# for x in mydict.values():
#     print(x)

# Printing key and values both
# for x,y in mydict.items():
#     print(x,y)
    
# add new key and vlaue pair in dict
# mydict["mobail_no"]=9898989898
# print(mydict)    

# mydict = {
#     101: "prashant",
#     "professional" : "Developer",
#     "empid" : 101
# }

# mydict.pop(101)  #pop() method removed pair by specific key names
# print(mydict)


# mydict = {
#     101: "prashant",
#     "professional" : "Developer",
#     "empid" : 101
# }

# newdict= mydict.copy()  
# print(newdict)


# def check_empty(mydict):
#     if mydict=={}:
#         print("Dict is empty")
#     else:
#         print("dict is not empty")    
# def max_value(mydict):
#     print(max(mydict))

# def reverse_list(mydict):
#     pass
    
# mydict = {
#    "a":20,
#    "b":30,
#    "c":40
#    }

# check_empty(mydict)
# max_value(mydict)

#================================================ LINEAR SEARCH ===========================================#

# def linearSearch(arr , target):
#     for i in range(len(arr)):#i= 6
#         if arr[i] == target:#7
#             return i 
#     return -1    

# arr = [1,2,3,4,5,7,6,8,9]
# target = 7 
# result = linearSearch(arr , target) # calling function , time complexity O[N], space complexity O[1]
# if result != -1:
#     print("Element found at index no = ",result)
# else:
#     print("Element not found")    

# why we check time complexity ---- > To check performance

# def maxvalue(arr):
#     max=arr[0]
#     for i in arr:
#         if max < i:
#             max = i
#     return i
        
# def minvalue(arr):
#     min=arr[0]
#     for k in arr:
#         if min > k:
#             min = k
#     return k          
# # error in cal min

# arr = [1,2,3,4,5]
# print(maxvalue(arr))
# print(minvalue(arr))


## majority of element

# def majorityElement(arr):
#     pass
    

#================================================== FILE HANDLING ===============================================# 

# why we use file handling?
# ------> whenever we have to use/store the data for future purpose so we use the file handling concept.

# Syntax for opening file ---> F = open(filename,mode)
# Mode ---> Read and Write and Append

# f = open("myfile.txt","w") # automaticaly create file if file doesn't exists (in write mode)
# print("name of file :",f.name)
# print("file mode :",f.mode)
# print("readable :", f.readable())
# print("writeable :", f.writable())
# print("file closed :", f.closed)
# f.close()
# print("file closed :",f.closed)

# f = open("myfile.txt","a") #here if we perform any changes in append mode it dosen't overwrite if we do in write mode it overwrite
# f.write("\n Pune is a smart city")
# f.write("\n Nagpur is a smart city")
# f.write("\n Jalgaon is a smart city")
# f.write("\n Banglore is a smart city")
# f.write("\n Nashik is a smart city")
# f.close()
# print("file operation is done")

# f = open("tryfile.txt","w")
# mylist=["Bhagya","rutuja","harsh"]
# f.writelines(mylist)
# f.close()
# print("written work has done successfully")

# #reading data from file
# f=open("myfile.txt","r")
# print(f.read())
# f.close()

# with open ("myfile.txt","w") as f:
#     f.write("amit\n")
#     f.write("ashish\n")
#     f.write("Prashant\n")
#     print("file closed: ",f.closed )
# print("file closed:",f.closed)    

# with open("myfile.txt","r") as f:
#     content=f.read()
#     print(content)


# =============================================== operation on image ========================================#

# f1=open("bhagya.jpg","rb") #rb --> read binary
# f2=open("nagane.jpg","wb") #wb --> write binary
# data = f1.read() #it will read its entire binary data of bhagya.jpg
# f2.write (data) #it will write entire data in nagane.jpg


# ================================================= OPERATION ON CSV ==========================================#
#difference between excel and csv ---> csv is lightweight it saves memeory than a excel file

import csv
# f = open("student.csv","a", newline="")
# a = csv.writer(f) # here it will return csv writer object
# # a.writerow(["studentID","rollno","name","mobileno"])#we always write a column name in string

# studentid = int(input("Enter student id :"))
# rollno = int(input("Enter roll number :"))
# name = input("Enter name :")
# mobailno = int(input("Enter mobail number :"))
# a.writerow([studentid,rollno,name,mobailno])
# print("student record has save")


# f = open("Marks.csv","a",newline="")
# a = csv.writer(f)
# a.writerow(["rollNo","name","mobailno","maths","phy","chem","total","percentage","email","result"])

# rollno = int(input("Enter roll no :"))
# name = input("enter your name :")
# mobailno = int(input("Enter your mobail no :"))
# maths = int(input("Enter your maths marks :"))
# phy = int(input("Enter your phy marks :"))
# chem = int(input("enter your chem marks :"))
# total = maths + phy + chem
# percentage = total/3.0
# email = input("enter your email :")

# if maths <= 40 and phy <= 40 and chem <= 40:
#     result = "pass"
# else:
#     result ="fail"    

# a.writerow([rollno,name,mobailno,maths,phy,chem,total,percentage,email,result])
# print("student record has save")




#=================================================== QUEUE ==============================================#

# import sys
# class Queue:
#     def __init__(self, queueSize): # parametrized constructor
#         self.queueSize = queueSize
#         self.myQueue = []

#     def isFull(self):
#         if  len(self.myQueue) == self.queueSize:
#             return True  
#         else:
#             return False

#     def isEmpty(self):
#         if self.myQueue == []:
#             return True
#         else:
#             return False
        
#     def enQueue(self, value):
#         if self.isFull():
#             print("Queue is Full")
#         else:
#             self.myQueue.append(value)   

#     def Display(self):
#         if self.isEmpty():
#             print("Queue is empty") 
#         else:
#             print(self.myQueue)           

#     def deQueue(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             self.myQueue.pop(0)            

#     def forntPeek(self):
#         if self.isEmpty():
#             print("Queue is empty")
#         else:
#             print(self.myQueue[0])

#     def emptyQueue(self):
#         self.myQueue.clear()

#     def deleteQueue(self):
#         self.myQueue = None

             
# size = int(input("Enter the size of Queue :"))
# queObj = Queue(size)
# while True:
#     print("1. enQueue")
#     print("2. Display")
#     print("3. deQueue")
#     print("4. frontPeek")
#     print("5. Empty Queue")
#     print("6. deleteQueue")
#     print("7.exit")
#     choice = int(input("Enter your choice :"))

#     if choice == 1:
#         value = int(input("Enter value to add in Queue :"))
#         queObj.enQueue(value)
#     elif choice == 2:
#         queObj.Display()
#     elif choice == 3:
#         queObj.deQueue()   
#     elif choice == 4:
#         queObj.forntPeek()
#     elif choice == 5:
#         queObj.emptyQueue()
#     elif choice == 6:
#         queObj.deleteQueue()    
#     elif choice == 7:
#         print("Exit...")
#         sys.exit()    
           