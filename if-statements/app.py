day_of_week = input("What day of the week is it? ")

if day_of_week.lower() == "monday":
  print("Have a great start of your week")
elif day_of_week.lower() == "friday":
  print("Have a good weekend!")
else:
  print(f"Have a good {day_of_week}")