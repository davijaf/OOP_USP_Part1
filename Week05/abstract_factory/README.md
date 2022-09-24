# Abstract Factory pattern (_Abstract Factory_)

Codes with examples of the Abstract Factory pattern (_Abstract Factory_) from the GoF book.

## Game theme change (Python)

The `game.py` file implements a game with 2 different theme types: Wild West and Space. Product families are defined for each theme and concrete factories are created for each of the two themes. When executing the script, it is possible to choose at runtime between the implemented themes and see the result of a small test for each product in the family.

## Creation of graphical components (Python)

The `gui.py` file implements an abstraction of creating different graphical components for different operating systems (GNU/Linux, Windows and MacOS). In this example, a `FactoryGUI` class is created which, when instantiated, configures which concrete classes to use for each component based on the detected operating system.

## Using the Abstract Factory Pattern in Python

Due to the fact that in the Python language classes and functions are first-order objects, that is, they can be stored in variables, passed as parameters and returned as the return value of functions, the implementation of most Creational Patterns can be replaced by use of other language features. A very concise example is described [in this article](https://python-patterns.guide/gang-of-four/abstract-factory/) from the `python-patterns.guide` page.