
# You can also import Tuples, Sets, etc... to use when type hinting
from typing import List

# You cant define what needs to be poased through like this 
# and the -> shows what it should return
def list_avg(sequence: List) -> float:
  return sum(sequence) / len(sequence)

list_avg((1, 2, 5))

class Book: 
  def __init__(self, name: str, page_count: int):
    self.name = name
    self.page_count = page_count

class BookShelf:
  # this will define that the book parameter should be a list of book objects
  # given the class book exists
  def __init__(self, books: List[Book]):
    self.books = books

  def __str__(self) -> str:
    return f"Bookshelf with {len(self.books)} books"