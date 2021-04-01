def shop():
  items = {
    "eggs": 1.99,
    "milk": 0.99,
    "cereals": 2.99,
    "steak": 4.79,
    "Beer": 2.99,
    "Sausage": 1.29,
    "Vinegar": 2.49,
    "Bread": 1.49
     }
  return items

def view_all(products ={}):
  for i in products:
    print(i)
