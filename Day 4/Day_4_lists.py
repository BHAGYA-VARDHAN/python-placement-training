# mylist = ["prashant","ashish","komal","ankush","ashish",77,"sandip",60.52,"prashant"]
# print(mylist)
# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])
# print(mylist[:])
# print(mylist[::-1])


# mylist[2] = "Akshay" # mutability of list, changing the value present at index 2 (komal)->(Akshay)
# print(mylist)

# if "ankush" in mylist:  #membership operator (in, not in), to check if the value is present or not
#     print("Present")
# else:
#     print("Absent")


# mylist.append("harsh") #inserts element at last
# mylist.append("laxman") 
# print(mylist)


# mylist.insert(1,"sanket") #inserts element at specified index
# print(mylist)

# mylist.remove("sandip") 
# print(mylist)

# newList = mylist.copy() #cloning
# print(newList)


# mylist = [['prashant','jha'],['85.56'],[440022,'yyy']]
# print(mylist)
# # print(mylist[row][col])
# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# list1 = ["prashant","jha"]
# # print(list1 * 2)
# list2 = [50,25.50]
# print(list1 + list2)

# list2 = [50,25.50,"prashant"]
# # del list2[2]
# del list2 # name 'list2' is not defined. Did you mean: 'list'?
# print(list2)


# list2 = [50,25.50,"prashant"]
# print(list2)
# list2.clear() #truncate in SQL, returns empty list
# print(list2)

# list2 = [50,25.50,"prashant"]

# #TYPECASTING to LIST
# name  = "Prashant"
# myName = list(name) #via list() constructor
# print(name)
# print(myName)


# mylist  = [40,30,20,10]
# mylist.reverse()
# print(mylist)

# mylist = [44,22,77,0,9,88]
# mylist.sort() # default -> ascending order sorting (L->H), pass arguement reverse = True for descending order (H->L)
# print(mylist)

# #default sorting order for numnber is ascending
# #default sorting order for string is alphabetical order
# # list should contain homogeneous data otherwise we we will get TypeError
# # python 2 supported the heterogeneous lists, sorts numbers first then strings 


# mylist = [44,22,77,0,9,88]
# newList = mylist #assigning the address
# print(id(mylist))
# print(id(newList))
# mylist[0] = "prashant"
# print(mylist)
# print(newList)

# name  = 'help4code'
# print('h' in name)
# print('z' in name)
# print('z' not in name)

# list3 = [10,20,30,40,50]
# for i in list3:
#     print(i)
    
# listNum = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in listNum:
#     sum += i 
# print("The sum of 1-10 is :",sum)


# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("This is my Purchased item")
#         continue #transfer statements: continue,pass and break.
#     print(i)

# mycart = [10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("This is my Purchased item")
#         break #transfer statements: continue,pass and break.
#     print(i)


# rollNo = [3,5,7,1,11,4,5,2]
# for x in rollNo:
#     if x==2 or x==4 or x==6 or x==8:
#         print("even number found :",x)
#         break
# # even number found : 4

