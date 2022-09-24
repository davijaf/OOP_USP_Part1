Examples of the Factory Method Pattern (_Factory Method_) from the GoF book.

## Python classes or types

In python classes or types, they are first-order objects that can be called and return an instance like this all basic types (`int`, `str`) and other Python standard library classes (`list`, `dict`) can be thought of as factories.

## Turtle (Python)

In the example of the `turtle.py` file that we used in the Strategy and Adapter Patterns, we had a python dictionary `STRATEGIAS_SALVAMENTO` that was responsible for providing the correct strategy to save the file. This dictionary combined with the line that instantiates the object can be interpreted as a functioning of the Factory Method pattern. In the `turtle.py` file the functionality was placed inside a function (method) named `select_strategy` to make explicit the use of the pattern.

The `turtle2.py` file shows an alternative implementation where the `select_strategy` method is placed inside the `FabricaStrategia` class, which initializes the collection of possible strategies in its creation. This strategy simplifies the process of creating new strategies that are automatically included in the factory if they are subclasses of `SaveScreen`.