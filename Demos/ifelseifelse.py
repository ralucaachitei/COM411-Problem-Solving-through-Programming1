print("What is your name?")
n = input()
#print ("Do you have a dog (type true or false"))
#dog = input()
#bool is boolean datatype - only stores true or false


if len(n) > 9: # allow lenght of exactly 9 and greater
  print ("You have a very loooong name!")
  print ("Your name contains {} letters".format(len(n)))
elif len(n) > 6:
  print ("Your name is a bit long. Consider a nickname")
elif len(n) < 3:
  print ("Your name is very shooort")
else:
  print("Your name is quite ok")
print("This is the end of the program!")