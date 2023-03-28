# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.
def reverseName(myName):
  newname = ''
  x = (len(myName))
  while x > 0:
    x = x-1
    newname = newname+myName[x]
  return str(newname)

def rootAge(myAge):
  return int(myAge)**2
  
me = input("What is your name? ")
im = input("What is your age? ")

print("Your name in reverse is: ",reverseName(me))
print("The square root of your age is: ",rootAge(im))
