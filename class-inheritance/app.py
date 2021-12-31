# Parent Class
class Device:
  def __init__(self, name, connected_by):
    self.name = name
    self.connected_by = connected_by
    self.connected = True

  def __str__(self):
    return f"Device: {self.name!r} ({self.connected_by})"

  def disconnected(self):
    self.connected = False
    print("Disconnected.")


# Child class of device class, you can still use the parent class with no problems
# the parent class has no idea the child class exists
class Printer(Device):
  def __init__(self, name, connected_by, capacity):
      super().__init__(name, connected_by)
      self.capacity = capacity
      self.remainning_pages = capacity

  def __str__(self):
      return f"{super().__str__()} ({self.remainning_pages} pages remaining)"
  
  def print(self, pages):
    if not self.connected:
      print("Your printer is not connected")
      return
    print(f"Printing {pages} pages")
    self.remainning_pages -= pages

printer = Printer("Printer", "USB", 500)
printer.print(20)

print(printer)

# the printer can still use the dissconnect method from the parents class
#  when it sees its not in the printer class it will look in the parents
#  and find it there 
printer.disconnected()
printer.print(30)