#list
#displaying elements of list

list1=[22,33,"HELLO","PYTHON"]
print(list1)
print(list1[1])
print(list1[0])
print(list1[2])
print(list1[3])
print(list1[-4])
print(len(list1)) #length of list
print(type(list1)) #type of list
print("..............................................")
#concatination of list
list2=[1,2,3,4]
list3=[9,8,7,6]
print(list2+list3)
print("..............................................")
#change value

list4=[10,20,30,40]
list4[1]=200
print(list4)
print("..............................................")
fruits=["apple","banana","orange"]
fruits.append("cherry")#adding elements in list ,append the element in last position
fruits.insert(1,"grapes")#adding elements in specified position
print(fruits)
print(len(fruits))
print(fruits.index("cherry"))
fruits.remove("grapes") #remove an element
fruits.pop(1) #remove an elements in particular index
del fruits[0] # delete an element in particular index
fruits.clear()#to completely clear a list
print("..............................................")