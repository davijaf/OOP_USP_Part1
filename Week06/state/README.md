# Default State (_State_)

Codes with examples of the State pattern (_State_) from the GoF book.

## Network Connections (C++)

In this code example created by Chris Sharver the State pattern is used to change the behavior of the class that models a TCP/IP connection (`TCPConnection`) according to the connection state: closed (`TCPClosed`), established (` TCPEstablished`) and listening (`TCPListen`).

The complete code can be found on [Chris Sharvers' website](https://www.evl.uic.edu/scharver/labreports/patterns/state.html#Known)

## PyFSM (Python)

PyFSM is a Python module that provides classes for developing event-driven applications. You can find the implementation of the State pattern in the file [`state\_machine.py`](https://github.com/jbarbadillo/pyFSM/blob/develop/pyfsmlib/state_machine.py) where the `State` classes are declared which represents a state and `StateMachine` the context class that uses the different states.

## FiniteStateMachine (Python/DSL)

Another example of using the State pattern is the software [FiniteStateMachine](https://wiki.python.org/moin/FiniteStateMachine).

This software allows the creation of a Domain Specific Language (DSL - _Domain Specific Language_) from the drawing of a state diagram.

The [tutorial](http://fsme.sourceforge.net/doc/tutorial.html) of the official software documentation has some examples of using the software and the generated DSL.