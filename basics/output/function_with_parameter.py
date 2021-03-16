#escape_by("jumping")
#escape_by("running around")
#escape by("going deeper")

#we cannot escape that way! The boulder is too big!
#we cannot escape that way! The boulder is moving too fast!
#that might work! Let's go deeper!

#This is function with single plan and name is 'plan'

def escape_by(plan):
  if(plan == "jumping over"):
    print("we cannot escape that way!The boulder is too big")
  elif(plan == "running around"):
    print("We cannot escape that way!The boulder is moving too fast!")
  elif(plan == "going deeper"):
    print("That might be a good idea!Let's do it")
  else:
    print("not sure about the plan")

#Call to the function

escape_by("jumping over")
escape_by("running over")
escape_by("going deeper")
escape_by("not sure about the plan")
escape_by("let's listen")