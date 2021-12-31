class ClassTest:
  def instance_meethod(self):
    print(f"Called instance_method of {self}")
  
  @classmethod
  def class_method(clas):
    print(f"Called class_method of {clas}")

  @staticmethod
  def static_method():
    print("Called static_method")

test = ClassTest()

# Both of these will call the isntance method
# Instance method is a function/method can be used to acces both the calss and instance
# used mainly for assigning or getting info from or too the class or modifying things in it
ClassTest.instance_meethod(test)
test.instance_meethod()

#  when the @classmethod is used you can make a function/method that can accesss
# the class inside the obj/class
# used mainly as factories
ClassTest.class_method()
test.class_method()

# Expl of factories
class Book:
  TYPES = ("hardcover", "paperback")

  def __init__(self, name, book_type, weight):
    self.name = name
    self.book_type = book_type
    self.weight = weight

  def __repr__(self):
    return f"<Book: {self.name}, {self.book_type}, Weight: {self.weight}g>"
  
  @classmethod
  def hardcover(cls, name, page_weight):
    return cls(name, cls.TYPES[0], page_weight + 100)
  
  @classmethod
  def paperback(cls, name, page_weight):
    return cls(name, cls.TYPES[1], page_weight)

# how ytou can do it without the use of factories
book = Book("Harry Potter", 'hardcover', 1500)
print(book.name)
print(book)

# how you create items objects that have factories
book_hardcover = Book.hardcover("Harry Potter", 1500)
book_paperback = Book.paperback("Harry Potter", 600)

print(book_hardcover)
print(book_paperback)




# When using the @staticmethod you are basically making a method/function in the class/obj 
# that wont have access to itself its just defining a seperate method that jsut so
# happens to be nested in that class/obj
# used mainly for code orgonization or when you feel like a method belongs there
ClassTest.static_method()
test.static_method()


















class Test:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
adam = Test("Adam", 25)

print(adam.age)

adam.job = "retail"

print(adam)
