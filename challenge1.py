#coding challenge 1
#1. Create a list of your favorite food items, the list should have minimum 5 elements.
#2. List out the 3rd element in the list.
#3. Add additional item to the current list and display the list.
#4. Insert an element named tacos at the 3rd index position of the list and print out the list elements

fav_food=["firedrice","biriyani","chappathi","porotta","burger","pizza"]
print("length of list ",len(fav_food))
print(fav_food)
print("---------------------")

print("third element = ",fav_food[2])
print("---------------------")

#adding additional element
fav_food.append("dosa")
print(fav_food)
print("---------------------")

fav_food.insert(3,"tacos")
print(fav_food)
