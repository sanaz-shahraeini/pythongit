#### Tuple :
# tuple haman list hast faghat gheire ghable taghyeer
## tuple : imutable (غیر قابل تغییر)
## list  : mutable (قابل تغییر)
# list1 = ["Fatemeh", "Arezoo"]
# print(type(list1))  # <class 'list'>
# tuple1 = ("Fatemeh","Arezoo")
# print(type(tuple1)) # <class 'tuple'>
# list1[1] = "Sanaz"
# print(list1) # ['Fatemeh', 'Sanaz']
# tuple[1] = "Sanaz" # TypeError : ejaze taghyeer nadarim
# print(tuple1)
#--------
# mazaya e tuple :
# 1- agar bekhahim listi dar toole ejraye barname bedoone taghyeer bemanad az tuple estefade mikonim
# 2- zamane tafsire tuple ha kamtar ast
#-----------------------------
#..... concat with + in tuples
# tuple1 = (10, 20, 30)
# tuple2 = (40, 50)
# new_tuple = tuple1 + tuple2
# print(new_tuple) # (10, 20, 30, 40, 50)
# #.....len() ----> tedade azaye tuple
# print(len(new_tuple)) #5
#
# #.... count(object) ---> tedade objecte morede nazar ra barmigardand
# tuple3 = (5, 1, 2, 1, 6, 3, 5, 1, 3, 10)
# print(tuple3.count(1)) #1
# #..........del----> kollan tuple morede nazar ra delete mikone
# del tuple3
# print(tuple3) # NameError
#-------------------------
# baraye kar rooye tak take azaye tuple mitavanim ba dastoore for inkaro anjam bedim
fosool = (0, "Bahar", "Tabestoon", "Payeez", "Zemestoon")
# for fasl in fosool:
#     print(fasl)
print(fosool[1]) #Bahar
print("Payeez" in fosool) #True
#-------------------------------
# Tuple 1 ozvi
tuple1 = (10)
print(type(tuple1)) #<class 'int'>
tuple2 = (10,)
print(type(tuple2)) #<class 'tuple'>

