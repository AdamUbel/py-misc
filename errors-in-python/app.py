def divide(dividend, divisor):
  if divisor == 0:
    raise ZeroDivisionError("Divisor cant be 0.")
  return dividend / divisor

students = [
  {"name": "Adam", "grades":[96, 75]},
  {"name": "Mark", "grades":[]},
  {"name": "Sam", "grades":[100, 89]}
]


# Try will run and if an error happens itll go to the except stage then the finally
# if try has no errors itll go to the else stage then the finally stage
try:
  for student in students:
    name = student["name"]
    grades = student["grades"]
    average = divide(sum(grades), len(grades))
    print(f"{name} averaged {average}")
except ZeroDivisionError:
  print(f"Error: {name} has no grades")
else:
  print("-- All Students averages calculated.--")
finally:
  print("-- End of calculation --")

# Custom error Classes
#  you name the class then  inherit the most relevant error class
# you can add your own code into it as well if needed
class TooManyPagesReadError(ValueError):
  pass


class Book:
  def __init__(self, name: str, page_count: int):
    self.name = name
    self.page_count = page_count
    self.pages_read = 0
  
  def __repr__(self) -> str:
      return (
        f"<Book {self.name},read {self.pages_read} pages out of {self.page_count}.>"
      )
  def read(self, pages: int):
    if self.pages_read + pages > self.page_count:
      raise TooManyPagesReadError(
        f"You tried to read {self.pages_read + pages} pages but this book only has {self.page_count} pages"
      )
    self.pages_read += pages
    print(f"you have now read {self.pages_read} pages out of {self.page_count}.")

python101 = Book("Python 101", 50)

try:
  python101.read(35)
  python101.read(50)
except TooManyPagesReadError as e:
  print(e)