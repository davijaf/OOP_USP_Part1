# Adapter Pattern (_Adapter_)

Codes with examples of the Adapter pattern (_Adapter_) from the GoF book.

## Math Class

The `math.py` file implements an example of using the adapter pattern to adapt the name of the methods present in the math module to the interface with the name of the modified functions.

## Turtle

The `turtle.py` file is the same code present in the example of the Strategy pattern (_Strayegy(85)_), in which we can see that each of the strategy classes are adaptations of the `save` method of the `Image` class, where they were adapted both the method name and the parameters that are passed.

## Cell phone chargers

The `charger.py` file shows sample code from the

[Adapter pattern Wikipedia page](https://en.wikipedia.org/wiki/Adapter_pattern).

In the code, two cell phone models are created (Iphone and Android), which use chargers and two different types of connectors (Lithning and Micro USB) and a class is created to adapt the use of the Micro USB standard to the Iphone, delegating the `use_micro_usb` paired with the `use_lightning` method.

## Lecture by Peter Ullrich

At the Python Conference 2017 (PyCon17) in Sweden, software engineer Peter Ullrich gave a talk on using design patterns in python ([link to video](https://www.youtube.com/watch?v= bsyjSW46TDg)).

In this talk he demonstrates the use of the Patterns: Adapter, Facade and Observer.

The Adapter pattern is presented in 3 versions in the files:
[`adapter\_okay.py`](https://github.com/PJUllrich/Design-Patterns/blob/master/adapter_okay.py),
[`adapter\_better. py`](https://github.com/PJUllrich/Design-Patterns/blob/master/adapter_better.py) and
[`adapter\_best.py`](https://github.com/PJUllrich/Design-Patterns /blob/master/adapter_best.py).