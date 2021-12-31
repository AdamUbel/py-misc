def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cant be 0.")

  return dividend / divisor


def add(x, y):
  return x + y


def calculate(*values, operator):
  return operator(*values)


result = calculate(20, 4, operator=divide)
print(result)

def search(sequence, expected, finder):
  for elem in sequence:
    if finder(elem) == expected:
      return elem
  raise RuntimeError(f"Could not find element with {expected}.")

friends = [
  {"name": "Adam", "age" : 25},
  {"name": "Sam", "age" : 28},
  {"name": "Bob", "age" : 24}
]

def get_friend_name(friend):
  return friend["name"]

print(search(friends, "Bob", get_friend_name))