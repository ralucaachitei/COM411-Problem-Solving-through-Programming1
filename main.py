def isPrime(x):
  for i in range(2,x):
    if x%i == 0:
      return False
  return True

def findPrime(beginning,finish):
  for j in range(beginning,finish):
    if isPrime(j):
      return j

x=6
y=12

print(f"The prime between {x} and {y} is {findPrime(x,y)}")


  








#print("What is the number?")
#x=int(input())
#if isPrime(x):
 # print(f"The number {x} is prime")
#else:
  #print("The number is not prime")

