friends = {"Bob", "Adam", "Alex"}
abroad = {"Bob", "Alex"}

# diffrence will take one set and removes the same items that match another 
local_friends = friends.difference(abroad)
print(local_friends)

local = {"Alex", "Mark", "Jarred"}
away = {"Joe", "Salene"}

# Union will combine two sets
all_friends = local.union(away)
print(all_friends)

art = {"Bob", "Joe", "Alex"}
science = {"Jarred", "Bob", "Salene"}

# Intersection will make a set based off of items that share two sets
art_and_science = art.intersection(science)
print(art_and_science)