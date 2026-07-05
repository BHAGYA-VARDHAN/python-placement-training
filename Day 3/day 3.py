#=================== Day 3: Exceptional Handling  ===================#

# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except ZeroDivisionError:
#     print("Error occurred while dividing the numbers with zero")

# except ValueError:
#     print("Error occurred while dividing the numbers with string or symbol")
#     print("Please enter valid number")
# print("Continuing the program after exception handling") 


#exception have 2 types ----> Pre-defined and user-defined
#if user try to divide a number with any symbol or string then it will give value error and 
#if user try to divide a number with zero then it will give zero division error


# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("plz ensure that you can't divide a number with zero")

# except ValueError as message:
#     print("Enter only valid no =>", message)
# print("Continuing the program after exception handling") 



#IMP QUE FOR INTERVIEW --> CAN WE HANDLE MULTIPLE EXCEPTION IN SINGLE EXCEPT BLOCK



#--------Here we can handle multiple exception in single except block by using tuple in except block---------#



# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Error occurred =>", message)  



#============ DEFAULT EXCEPTION HANDLING =============#



# NOTE - Default exception block must be in last of code  otherwise syntax error will occur

# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Error occurred =>", message)
# except:
#     print("This is a default part of exception block")


# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except:
#     print("This is a default part of exception block")    
# except (ZeroDivisionError, ValueError) as message: #here syntax error will occur because default exception block must be in last of code
#     print("Error occurred =>", message)

# we have else block in exception handling which will execute if try block is executed successfully without any error
# for Example - if user enter valid number then else block will execute otherwise except block will execute
# it is depend on our own needs and neccessity


# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Error occurred =>", message)
# else:
#     print("Everything is okay")    



#============ FINALLY BLOCK =============#



# finally block will always execute whether try block is executed successfully or not
# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Error occurred =>", message)
# finally:
#     print("I will always executed")    



#======== NESTED TRY EXCEPT BLOCK ==========#



# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     try:    
#         print(a/b)
#     except ZeroDivisionError as message:
#         print("Error occurred =>", message)
# except ValueError as message:
#     print("Error occurred =>", message)


#----------WITH ELSE AND FINALLY BLOCK----------#


# try:
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))    
#     print(a/b)
    
# except (ValueError, ZeroDivisionError) as message:
#     print("Error occurred =>", message)
# else:
#     print("Everything is okay")    
# finally:
#     print("I will always executed")



#=============================== USER DEFINED EXCEPTION =================================#



# bank_bal = int(input("Enter your bank balance : "))
# if bank_bal < 1000:
#     raise Exception("Insufficient Balance")  # By raise keyword we can raise our own exception
# else:
#     print("You can withdraw your money")



# ============================= LOG FILE IN PYTHON (LOGGING) ==============================#

#Why we used filed handling ---> to store the data permanantly in file and we can use it for future reference

#python logging level
# import logging

# logging.basicConfig(filename='newfile.txt',level= logging.DEBUG)
# logging.debug("this indicates the debugging info")
# logging.info("this indicates the important info")
# logging.error("this indicates the error info")
# logging.warning("this indicates the warning info")
# logging.critical("This indicates the critical info")


# import logging

# try:
#     logging.basicConfig(filename='arithmatic.txt',level= logging.DEBUG)
#     a = int(input("Enter value of A : "))
#     b = int(input("Enter value of B : "))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print("Error occurred =>", message)
#     logging.exception(message)

# print("Logging level is set up. Check the file arithmatic.txt for the log messages.")


# TASK = write a program to accept 3 paper marks likt phy , chem, math and cal total, percentage and display total marks, percentage.
# condition
# if user is passed in all sub then print pass else print fail and passing marks is 40
# if percentage is greater than equal to 65 and gender is male then print you are eligibe for placemnet else not eligible for placement.

# phy=int(input("Enter phy marks : "))
# chem=int(input("Enter chem marks : "))
# math=int(input("Enter math marks : "))
# total = phy + chem + math
# per = total/3.0

# print("Total Marks=", total)
# print("Total Per=", per)

# #condition one
# if phy>=40 and chem>=40 and math>=40:
#     print("Pass")
# else:
#     print("Fail")

# #condition two
# gen=input("Enter your gender M/F : ")
# if per>=65 and gen == 'M':
#     print("You are eligible for placement")
# else:
#     print("you are not eligible for placement")    
