#  You can assign the deafult paramater in the 
# function arguments so if no other argument is assigned it will use the default
from typing import Sequence


def add(x, y=8):
  return x + y

print(add(5))
print(add(5, 6))

# functions return "NONE" by default unless you use the return keyword

# Lambda Function
def subtract(x, y):
  return x - y

print(subtract(5,7))



# you can add a name if wanted but without a name you need to use it in the same line
print((lambda x, y: x + y)(5, 12))

def doubled(x):
  return x * 2

sequence = [1, 3, 5, 9]
doubled_list = [doubled(x) for x in sequence]
print(doubled_list)

doubled_list2 = list(map(lambda x: x * 2, sequence))
print(doubled_list2)