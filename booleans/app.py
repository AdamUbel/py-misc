print(5 == 5)
print(5 > 5)
print(10 != 10)

# Comparisons: ==, !=. <, >, <=, >=

friends = {"Adam", "James"}
away = {"Adam", "James"}

print(friends == away)

# Will return false because sets are made seperatly
# you can make away = friends and then the is would return true
print(friends is away)
print(friends is friends)