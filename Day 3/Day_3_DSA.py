#========================================== DSA ========================================#
# Q. What is data structure?
#--> data structure are diiferent ways of organizing data on your computer, that can be used effectively.
# Q, what are the features you have ti check in algorithm?
#--> corretness and efficiency
# Q. where we can use dsa?
#--> in Business logic layer


#Big O --> Best case
#big Omega --> Avg. case
#Big Theta --> Worst case

# O(1) --> Constant time (accessing a specific element in array)
# arr=[1,2,3,4,5]
# arr[0] #it takes constant time to access 1st element


#O(N) --> Linear time (loop through array element)
# arr=[1,2,3,4,5]
# for element in arr:
#     print(element)
# linear time since it is visiting every elememt of arr    


#O(LogN) --> Logarithmic time (find an element in sorted array, eg. binary search)
# arr=[1,2,3,4,5]
# for index in range (0, len(arr),3):
#     print(arr[index])
# logarithmic time since it is visiting only some specific element    


#O(N^2) --> Quadratic time (Looking at a every index in the array twice)
# arr=[,2,3,4,5]
# for x in arr:
#     for y in arr:
#         print(x,y)

# wrost case scenario we always try to avoid nested for loop


#O(2^N) --> exponential time (Double recursion in Fibonacci)
# def fibonacci(n):
#     if n <= 1:
#         return n
#     return fibonacci(n-1) + fibonacci(n-2)

# import sys
# def add():
#     a = int(input("Enter value of A :"))
#     b = int(input("Enter value of B :"))
#     print(a+b)

# def sub():
#     a = int(input("Enter value of A :"))
#     b = int(input("Enter value of B :"))
#     print(a-b)

# def div():
#     a = int(input("Enter value of A :"))
#     b = int(input("Enter value of B :"))
#     print(a/b)            
        
# def mul():
#     a = int(input("Enter value of A :"))
#     b = int(input("Enter value of B :"))
#     print(a*b)        

# while True:
#     print("1. Addition ")
#     print("2. Substraction ")
#     print("3. Division ")
#     print("4. Multiplication ")
#     print("5. Exit ")

#     choice = int(input("Enter your choice : "))

#     if choice == 1:
#         add()#calling add function
#     elif choice == 2:
#         sub()#calling sub function
#     elif choice == 3:
#         div()#calling div function
#     elif choice == 4:
#         mul()#calling mul function      
#     elif choice == 5:
#         sys.exit()#exit the program


# arr = [1,2,3,4,5]
# prod = []
# mul = 1
# for i in range(len-1):
# incomplete


#====================================STACK IMPLEMENTATION USING SIZE LIMIT===================================#
# operation of stack -->
# Push
# pop
# isEmpty
# isFull
# Display

# import sys
# class stack:

#     def __init__(self,stackSize):
#         self.stackSize = stackSize #stack size define
#         self.myStack = [] # list represent stack
#         print("Stack as created")

#     def isFull(self):
#         if len(self.myStack) == self.stackSize:
#             return True
#         else:
#             return False
        
#     def isEmpty(self):
#         if self.myStack == []:
#             return True
#         else:
#             return False
            
#     def push(self, value):
#         if self.isFull():
#             print("             Stack is full            ")
#         else:
#             self.myStack.append(value)    

#     def display(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print("stack =",self.myStack)           

#     def Pop(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack.pop()) # here instead of pop() we can use [-1] 

#     def Peek(self):
#         if self.isEmpty():
#             print("stack is empty")
#         else:
#             print(self.myStack[-1])  

#     def Delete(self):
#         self.myStack = None               


# size = int(input("Enter the size of stack :")) 
# obj = stack(size)

# while True:
#     print("1. Push")
#     print("2. Display")
#     print("3. Pop")
#     print("4. peek")
#     print("5. Delete")
#     print("6. Exit")
#     choice = int(input("Enter your choice : "))
#     if choice == 1:
#         value = int(input("Enter the value to push in stack : "))
#         obj.push(value)
#     elif choice == 2:    
#         obj.display()
#     elif choice == 3:
#         obj.Pop()
#     elif choice == 4:
#         obj.Peek()    
#     elif choice == 5:
#         obj.Delete()
#     elif choice == 6:
#         sys.exit()


#stack using list
# -- easy to implement 
# -- speed problem

# print('Bhagyavardhannagane1806'.isalnum()) #alphanumeric
# print('Bhagyavardhannagane'.isalpha())
# print('006f'.isdigit())
# print('Bhagyavardhannagane'.islower())
# print("".islower())
# print('BHAGYA'.isupper())
# print(' MY Name is Bhagyavardhan'.istitle())
# print(''.istitle())
# print(''.isspace())
# print("Hello".startswith("He"))
# print('Hello'.endswith("lo"))

