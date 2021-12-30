name = "Bob"
greeting = f"Hello, {name}"

print(greeting)

name = "Adam"

print(greeting)
print(f"Hello, {name}")

greeting_two = "Hello, {}"
with_name = greeting_two.format("Charley")

print(with_name)

longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Adam", "Monday")

print(formatted)