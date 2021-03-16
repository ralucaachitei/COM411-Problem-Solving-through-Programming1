def isPrime(x):
  for i in range(2,x):
    if x%i == 0:
      return False
  return True

print("What is the number?")
x=int(input())
if isPrime(x):
  print(f"The number {x} is prime")
else:
  print("The number is not prime")

