def divide(dividend, divisor):
  return dividend / divisor


# __name__ is a global varible in python that will change depending on what file youre in
# it will be able to let you know and differentiate between the file you run or
# a file you import
print("mymodule.py: ", __name__)

import libs.mylib