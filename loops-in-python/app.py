# While Loop
number = 7
while True:
  user_input = input("Would you like to play? (Y/n): ")

  if user_input.lower() == "n":
  # if user_input in ("n", "N"):
    break

  user_number = int(input("Guess our number: "))
  if user_number == number:
    print("You Guessed Right!")
  elif abs(user_number - number) == 1:
    print("You where off by 1")
  else:
    print("Sorry, you are wrong.")


# For Loop
friends = ["Adam", "Sam", "James", "Mark"]

for friend in friends:
  print(f"{friend} is my friend")

for number in range(10):
  print(number)


# for loop to add up everything in a list
grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
  total += grade

print(total / amount)

# alternate way is just using sum method on the list
sum(grades)