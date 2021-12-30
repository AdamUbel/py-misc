x = (5, 11)


#  you can assign tuples values to individual variables
y, z = x
print(y, z)


# this will destructure the items and make them tuples you can select from
student_attendance = {"Adam": 96, "Mark": 85, "Sam": 100, "Bob": 75}

for student, attendence in student_attendance.items():
  print(student)
  print(attendence)

#  this will take a list of tuples and allow you to 
# destructure it into other variables as well

people = [("Adam", 96, "Student"), ("Mark", 85, "Student"), ("Sam", 100, "Student"), ("Bob", 75, "Student")]

for name, grade, title in people:
  print(f"Name: {name}, Grade: {grade}, Title: {title}.")


# the star will collect all the other values in tail
head, *tail = [1, 2, 3, 4, 5]

print(head)
print(tail)