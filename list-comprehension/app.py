numbers = [1, 3, 5]
doubled = []

# forloop method in most langauges 
for num in numbers:
  doubled.append(num * 2)

# Python option
tripled = [n * 3 for n in numbers]
print(tripled)

friends = ["Adam", "Steve", "Matt", "Sam", "Jerry"]
starts_s = []

for friend in friends:
  if friend.startswith("S"):
    starts_s.append(friend)

print(starts_s)

starts_s2 = [friend for friend in friends if friend.startswith("S")]

print(starts_s2)

friends_id_test = ["Adam", "Steve", "Matt", "Sam", "Jerry"]
friends_id_test2 = ["Adam", "Steve", "Matt", "Sam", "Jerry"]

# even though they contain the same this the is statement will see them as diffrent
print(friends_id_test is friends_id_test2)
print("friends 1:", id(friends_id_test), "friends 2:", id(friends_id_test2))