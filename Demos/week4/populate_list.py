def directions():
  directions = ["Move forward", "Move backwards", "Turn Left", "Turn Righ"]
  return directions

def menu():
  print("please select a direction:")
  dirs = directions()
  for index in range(len(dirs)):
    print("{}: {}". format(index, dirs[index]))
  index = int(input())
  return dirs[index]

def run():
  route = []
  print("Working out escape route...")
  for count in range(5):
    route.append(menu())
  print("Escape route: {route}")
  
run()

