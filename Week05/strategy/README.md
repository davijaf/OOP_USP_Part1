# Strategy Pattern (_Strategy_)

Codes with examples of the Strategy pattern (_Strategy_) from the GoF book.

## Examples

### Turtle (Python)

Code that generates an interactive canvas (_Canvas_) from the Python `turtle` module and uses different strategies to save drawings made with different file formats.

Use the arrow keys to move the turtle and press the `s` keys to open the menu to save the file

To run this code, it is necessary to install the `Pillow` module, using the `pip install pillow` command. It is not necessary to do this step if you have already installed the project's dependencies through the command `pip install -r requirements.txt`

**Note**: For this example to work on Windows it is necessary to install the `ghostscript` software. Instructions for installation and configuration can be found [here]
(https://gitlab.com/ccsl-usp/LabPOO/#guia-de-instala%C3%A7%C3%A3o-do-ghostscript-para-windows)

### Duck Simulator (Python)

Example adapted from the book "_Head First Design Patterns_"(HFDP).

The file `duck.py` has an implementation that is closer to the original implementation of the book (in Java language) and the file `duck_pythonic.py` makes an implementation using features present in the python language that are not present in the Java language (Inheritance multiple)

### SQLAlchemy (Python)

An example and real python software that implements the strategy pattern is the SQLAlchemy module.

SQLAlchemy is a suite of SQL and _Object Relational Mapper_(ORM) tools.

Its main use is to be an intermediate layer between the python language application and the SQL database used.

SQLAlchemy is free and open source software maintained by a large community, you can learn more by going to [project page](https://www.sqlalchemy.org/) and see the source code on its [GitHub]
(https://github.com/sqlalchemy/sqlalchemy).

As it is a highly complex software, the code is quite extensive and equally complex, to make it easier to see below, here are some examples of using the strategy pattern in the source code (with links to the classes)

The use of the strategy pattern can be noticed in the implementation of the class[`StrategizedProperty`](https://github.com/sqlalchemy/sqlalchemy/blob/575b6dded9a25fca693f0aa7f6d7c6e735490460/lib/sqlalchemy/orm/interfaces.py#L546) which models properties that can be strategized (contexts).

An example of such a property is the database columns, modeled in the [`ColumnProperty`] class(https://github.com/sqlalchemy/sqlalchemy/blob/58dc9c00133e13e5690e686e680b8275f162aded/lib/sqlalchemy/orm/properties.py#L40 ), subclass of `StrategizedProperty`.

The [`LoaderStrategy`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/interfaces.py#L827) class is used as the basis for the data load strategy classes.

So the strategies

[`ColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L175),

[`UninstrumentedColumnLoader`](https://github. com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L130),

[`ExpressionColumnLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L261),

[`DeferredColumnLoader`](https://github.com/sqlalchemy /sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L344),

[`AbstractRelationshipLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies. py#L531) and

[`DoNothingLoader`](https://github.com/sqlalchemy/sqlalchemy/blob/29575552b04f4d4e4f7373a8ddcaa2572046029e/lib/sqlalchemy/orm/strategies.py#L546) can be used with the context class `ColumnProperty` .