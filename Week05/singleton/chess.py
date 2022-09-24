# Function to test if a variable stores a class
from inspect import isclass


class Board:
     """
     Class that models a board in a chess game.
     """
     _instance = None

     # __new__ method changed to only create an instance of the class
     def __new__(cls):
         if cls._instance is None:
             cls._instance = object.__new__(cls)
         return cls._instance


if __name__ == '__main__':
     t1 = Board()
     t2 = Board()
     print(f'Variables t1 and t2 refer to the same object: {t1 is t2}')
     print(f'The class of t1 is: {type(t1)}')
     print(f'Board is class: {isclass(Board)}')