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
