#  when that argument is defined with a star it can take as many as needed when called
def multiply(*args):
  print(args)
  total = 1
  for arg in args:
    total = total * arg

  return total

print(multiply(1, 3, 5))


# you can also use it to descruter a list and oush it into a function with te same 
# amount of args as in the list 

def add(x, y):
  return x + y

# without the star it passess one value and that would be to the x arg
nums = [3, 5]
print(add(*nums))

# You can also do it with dictionaries if the key is the same name as the arg

dict = {"x": 5, "y": 12}
print(add(**dict))

# The alternate would be writing it like this
print(add(dict["x"], dict["y"]))


# when you use the *args paired with another named argument you have to name that argument
# when calling hte function

def apply(*args, operator):
  if operator == "*":
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No Valid operator provided to apply()"

print(apply(1, 3, 6, 7, operator="*"))
print(apply(1, 3, 6, 7, operator="+"))
print(apply(1, 3, 6, 7, operator="/"))

# Unpacking KEYWORD arguments
# usual names for arg is *args and keyword arguments is **kwargs
def named(**kwargs):
  print(kwargs)

# this will print a dictionary with the key as the keyword and the value as the arg
named(name="Bob", age=25)

def print_nicely(**kwargs):
  named(**kwargs)
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_nicely(name="Adam", age=25)

#  you can do both in one function the positional args will be stored 
# in *args and the named arguments will be storeed in **kwargs

def both(*args, **kwargs):
  print(args)
  print(kwargs)

both(1,2,3, name="Matt", age=34)