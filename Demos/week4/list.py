
fruits = {}

#Define a list with items

vegetables = ["Carrot", "Peas"]

#Add items to the list
fruits.append("Apple")
fruits.append("Bannana")
fruits.append("Tomatoes")
fruits.append("Banana")
print(fruits)

#Remove an item from the list
fruits.remove("Banana")
print(fruits)

#Remove item from index
del fruits[1]
print(fruits)

#Insert a value not at the end
fruits.insert(1, "Pineapple")
print(fruits)

#Access single element
print(fruits[0])


def get_fruits():
  fruits = []
  print("How many fruits would you like to enter?")
  n = int(input())
  for i in range(n):
    print("type in the next fruit:")
    fruits.append(input())

  #Print all items
  print("Your fruits are {}".format(fruits))
  #Print few items by Slicing
  print(f"Sliced list: {fruits[0:5]}")

  #Print only few items using negative index
  print(f"Negative index: {fruits[-2:0:-1]}")


get_fruits()
