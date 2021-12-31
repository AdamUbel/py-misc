a = []
b = a

print(id(a))
print(id(b))

a.append(35)

print(a)
print(b)


# Mutable default parameters

from typing import List

class Student:
  # You dont want to define list to an empty list in the argument area
  # that will make it asign the same list to all students due to it bieng mutable
  #  in this case you want to assign the empty lsit when self.grades is defined
  # this will make a list for each student when being called
  def __init__(self, name: str, grades: List[int] = None): 
    self.name = name
    self.grades = grades or []

  def take_exam(self, result: int):
    self.grades.append(result)

bob = Student("Bob")
adam = Student("Adam")
bob.take_exam(90)
print(bob.grades)
print(adam.grades)

    