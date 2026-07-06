#===============================================  Argument ===========================================#

# =============== Positional argument =============== 
# def msg(val1, val2):
#     print("value 1=", val1)
#     print("value 2=", val2)
# #calling function
# msg("admin","help4code")    


# ================ Keyword Argument ================
# def msg(val1, val2):
#     print("value 1=", val1)
#     print("value 2=", val2)
# # calling function    
# msg(val1 = "admin", val2 = "help4code")


# ================ Default Argument =================
# def city(cityName="Nagpur"):
#     print("City Name =", cityName)

# city("Mumbai")
# city("Delhi")
# city()       # if we dont pass any default argument (city(cityName="Nagpur")) then it throws error


# ================= Variable length argument / Variable number of argument =================
# def cityName(*city):
#     print(city)

# cityName("Nagpur","Nashik","Pune","Delhi","Indore")
#TypeError: cityName() takes 1 positional argument but 5 were given -- if we not given / pass 'Variable length argument' --> cityName(city)


# def arithmatic(a, b):
#     add = a+b
#     sub = a-b
#     mul = a*b
#     div = a/b
#     return add,sub,mul,div #return multiple value at same time

# print(arithmatic(5,5))





