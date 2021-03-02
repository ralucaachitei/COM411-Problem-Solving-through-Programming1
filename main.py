print("What is your name?")
#Variable is a constainer which can store data for us in the memory(string, integer, float, boal)
name = input()
print("What is your age?")
age = int(input())
print("what is your bank balance?")
balance = float(input())

print("Welcome {}. You said to be {} years old. Your bank balance is {}.". format(name, age, balance))