# can be changed or modified
list = ["Bob", "Adam", "Alex"]
# Can't be changed or modified
tuple = ("Bob", "Adam", "Alex")
# can only have a value once and dont have an order
set = {"Bob", "Adam", "Alex"}

print(list[0])
print(tuple[1])

# adds to the list
list.append("Smith")
# removes from list
list.remove("Bob")

# adds to a set but if you add it twice it wont show a duplicate
set.add("Smith")
set.add("Smith")

print(list, set, tuple)