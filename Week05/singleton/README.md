# Singleton pattern

Codes with examples of the _Singleton_ pattern from the GoF book.

## About using (and implementing) the _Singleton_ Pattern in Python

As it is not possible to implement private attributes and methods in Python (including constructors), there are different strategies for implementing the _Singleton_ pattern.

You can find the main strategies in this
[StackOverflow thread] (https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python)
where each variant and their respective advantages and disadvantages are explained in detail.

In the following examples we use the implementation that changes the functioning of the `__new__` method in python, responsible for creating the objects of your class, always returning the same object.

To understand the flow of execution of the examples in code, it is necessary to understand the differences between the `__init__` and `__new__` methods of the Python language that you can read
[in this StackOverflow topic](https://en.stackoverflow.com/questions /177882/qual-%C3%A9-a-difference%C3%A7a-between-init-and-new).

## Computer graphics software (Python)

An example of using this late-instantiated _Singleton_ pattern implementation can be found in the
[`Shaders`](https://github.com/mjck/mac420/blob/d8c29be0be461144b93ef94d6cd289208bbc3bdf/Source/Graphics/Shaders.py#L5)
class of code repository for the MAC-420 Introduction to Computer Graphics course provided by Professor Marcel Jackowski (IME-USP).

## Chessboard (Python)

The `chess.py` file shows the implementation of this method correcting the problem of the object class returned (which in the previous example is different from the declared one), for the creation of a chessboard (video example)