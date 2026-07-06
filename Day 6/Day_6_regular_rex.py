
# =============================================== MATCH() Function =======================================

# import re
# count = 0
# pattern = re.compile(input("Enter the word you want to find: "))
# # print(pattern)
# matcher = pattern.finditer("In mathematics, a function defines a clear relationship between input and output. " \
#                            "Every function serves a purpose, mapping values with precision. " \
#                            "Without function, systems lose structure and meaning.")

# # print(matcher)
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurances: ",count)    


# -------------------------------------------------------------------------------------

# import re
# count = 0
# matcher = re.finditer("Hi","HiHiHiHi")
# # print(matcher)
# for i in matcher:
#     count+=1
# print("The number of occurances: ",count)    
#     print(i.start(),"...",i.end(),"...",i.group())


# -------------------------------------------------------------------------------------


# import re
# sentence = input("Enter the Paragraph: ")
# obj = input("enter any sentence")
# objmatch=re.finditer(obj,paragraph)
# #print(objmatch) 
# for match in objmatch:
#     print(match.start(),"...",match.end(),"...",match.group())


# -------------------------------------------------------------------------------------


# import re
# a = input("enter string to perform match operation :")
# mtch = re.match(a, "python is a very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at begining level")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("There is no match found at begining level ")    


# =============================================== FULL MATCH() ===============================================


# import re
# a = input("enter string to perform match operation: ")
# mtch = re.fullmatch(a, "Bhagyavardhan")
# print(mtch)
# if mtch!=None:
#     print("Match found")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("Full match not found")    


# =============================================== SEARCH() ====================================================

# import re
# a = input("enter string to perform match operation: ")
# mtch = re.search(a, "Bhagyavardhan learns python")
# print(mtch)
# if mtch!=None:
#     print("Match found")
#     print(mtch.start()," ", mtch.end())
# else:
#     print("There is no matching anywhere")  