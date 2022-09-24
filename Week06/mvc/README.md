# Pattern-View-Control (MVC)

Examples of using the Model-View-Controller design pattern

## Hangman (Python)

An example of game building using the MVC pattern is a hangman game, which can be found [in this Github repository]
(https://github.com/manuphatak/python_hangman).

Inside the `hangman` directory you can find the files `model.py` (Model), `view.py` (View) and `controller.py` (Controller).

## People registration system (Python)

The `people.py` file shows an example of a people registration system that implements the MVC pattern.

The Model part can be seen in the `Model` class (and its subclasses) together with the `database` dictionary which is used to simulate a database. The `Controller` class defines the execution flow from the commands given by the user (it could have been implemented as a function, but the class was used to demonstrate its role) and the views are made by the `MainPage` class and its subclasses.

## Internet blog (Python)

The MVC pattern is probably the most popular design pattern for creating web applications, so many programming languages ​​have several specific frameworks_ for this purpose: Flask and Django in Python, Rails and Sinatra in Ruby, Laravel in PHP and Spring in Java .

In this example we create two versions of a small blog application based on [this tutorial](http://turing.com.br/material/flask/tutorial/folders.html) from _framework_ Flask.

Flask is a _microframework_ in Python that implements the MVT (_Model-View-Template_) pattern, a variation of the MVC pattern.

In both versions, in the `flaskr.py` file we define our `app` controller, where we register our routes, and the views are the files present in the `templates` folder. Note that although the template files have the `.html` extension they are template files from the Python language `Jinja` library, which creates files that merge HTML _tags_ with python code to generate dynamic views.

In version 1 the model is only represented in the database connection by the `conectar_bd` function and all operations on the data are performed by the controller within the route. In the second version of the code, we used together with Flask the _framework_ SQLAlchemy, which provides a mapping of the classes defined with the database, so the model in question is the _post_ of the blog represented by the `Post` class (which inherits its basic of the `bd.Model` class).