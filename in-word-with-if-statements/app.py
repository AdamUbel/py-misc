movies_watched = {"The Matrix", "Harry Potter", "Green Book"}
user_movie = input("Enter A Movie You Watched Recently: ")

if user_movie in movies_watched:
  print(f"I've watched {user_movie} too.")
else:
  print("I haven't watched that yet")

number = 7
user_input = input("Enter 'y' if you want to play: ")

if user_input in ("y", "Y"):
  user_number = int(input("Guess our number: "))
  if user_number == number:
    print("You Guessed Right!")
  elif abs(user_number - number) == 1:
    print("You where off by 1")
  else:
    print("Sorry, you are wrong.")