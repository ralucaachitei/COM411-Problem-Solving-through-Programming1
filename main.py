import matplotlib.pyplot as plt

def coordinate():
  print("please enter an x value:")
  x=int(input())

  print("please enter a y value:")
  y=int(input())
  return(x,y)
def path():
  print("retriving path...")
  x_values=[]
  y_values=[]
  for count in range (4):
    data=coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return [x_values, y_values]
def run():
  values=path()
  plt.plot(values[0],values[1],"r--o")
run()










