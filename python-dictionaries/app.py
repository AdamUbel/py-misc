friend_ages = {"Adam": 24, "Alex": 24, "Matt": 27}

friend_ages["Sam"] = 30
print(friend_ages["Sam"])


print(friend_ages["Matt"])

friends = [
  {"id": 0, "name": "John", "Age": 34},
  {"id": 1, "name": "Sam", "Age": 30},
  {"id": 2, "name": "Clint", "Age": 36},
  {"id": 3, "name": "Mary", "Age": 32}
]

for friend in friends:
  print(friend["name"])

print(friends[1]["Age"])


student_attendance = {"Adam": 96, "Mark": 85, "Sam": 100, "Bob": 75}

# looping through the keys and values 
for student, attendance in student_attendance.items():
  print(f"{student}: {attendance}%")


# checking if the key exists then doing something
if "Bob" in student_attendance:
  print(f"Bob: {student_attendance['Bob']}%")
else:
  print("Bob isnt a student here.")

# get just values back withou knowing keys and printing sum
attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))


# Dictionary comprehesion

users = [
  (0, "Bob", "password"),
  (1, "Adam", "1234"),
  (2, "Alex", "password123"),
  (3, "Matt", "longpassword")
]

# destructers the list and adds the user as a key to the tuple
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your Username: ")
password_input = input("Enter your Password: ")

# checks the input with the tuple and will make sure they match
_, username, password = username_mapping[username_input]

if password_input == password:
  print("Your details are correct")
else:
  print("Your details are incorrect")