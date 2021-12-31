student = {"name": "Adam", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
  return sum(sequence) / len(sequence)

print(average(student["grades"]))


class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def average_grades(self):
    return sum(self.grades) / len(self.grades)

student_obj = Student("Adam", (89, 90, 85, 78, 84))
student_obj2 = Student("Bob", (87, 80, 95, 54, 82))

print(student_obj.average_grades())
print(student_obj2.average_grades())


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"Person: {self.name}, Age: {self.age} years old"
    

bob = Person("Bob", 35)

print(bob)
