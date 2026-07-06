# ============================================ Tuple =========================================#
# for i in range (1,4): #outer loop ==> Rows
#     for j in range(1,4): #inner loop ==> columns
#         print(i,end=" ")
#     print()    

# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print() 
    
#output
# 1 1 1 1 1 
# 2 2 2 2 2 
# 3 3 3 3 3 
# 4 4 4 4 4 
# 5 5 5 5 5 


# ------------------ Reverse the output -------------- #


# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

#output
# 5 5 5 5 5 
# 4 4 4 4 4 
# 3 3 3 3 3 
# 2 2 2 2 2 
# 1 1 1 1 1  


# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     print("*"*i)

#output
# *
# **
# ***
# ****
# *****


# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(chr(64+i),end=" ")
#     print()

# output
# A 
# B B 
# C C C 
# D D D D 
# E E E E E     

# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print("*",end=" ")
#     print()

# output
# * * * * * 
# * * * * 
# * * * 
# * * 
# *    


# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(64+j),end=" ")
#     print()

# output
# A B C D E 
# A B C D 
# A B C 
# A B 
# A     


# import time
# n = int(input("Enter the number of rows : "))
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         time.sleep(2)      # delay by 2 sec
#         print(n+1-i,end=" ")
#     print()    

# output
# 5 5 5 5 5 
# 4 4 4 4 
# 3 3 3 
# 2 2 
# 1     

# n = int(input("Enter the number of rows :")) #n=5
# for i in range(1,n+1):
#     for j in range(1,n+2-i):
#         print(chr(65+n-i),end=" ")
#     print()

# output
# E E E E E 
# D D D D 
# C C C 
# B B 
# A     


import time
n=int(input("Enter the number of row: "))
for i in range(1,n+1):
    print(" "*(n-i),end=" ")
    for j in range(1, i+1):
        time.sleep(2)
        print("*",end=" ")
    print()   

# output
#      * 
#     * * 
#    * * * 
#   * * * * 
#  * * * * *
     
