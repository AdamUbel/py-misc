# You cant call functions before theyre defined
def hello():
  print("Hello!")

hello()

def user_age_seconds():
  user_age = int(input("Enter Your Age: "))
  age_seconds = user_age * 360 * 24 * 60 * 60
  print(f"Your age in seconds is {age_seconds}.")

user_age_seconds()

# If you define an argument it needs to be fulfilled 
def add(x, y):
  return x + y

print(add(5, 7))

# You can attach keyword arguments when calling a function if needed
# this will allow you to label arguments out of order for the function when called

def divide(dividend, divisor):
  if divisor != 0:
    print(dividend / divisor)
  else:
    print("Youl Fool")

divide(divisor=0, dividend=15)