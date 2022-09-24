# Factory Method Pattern (_Factory Method_)

Examples of the Prototype (_Prototype_) design pattern from the GoF book.

## The `copy` module in Python

The standard python language library has a module called `copy` that has functions that allow copying objects: `copy(x)` and `deepcopy(x)`.

The main difference between these two functions is that the `copy(x)` function makes a "shallow" copy of object `x`, i.e. it copies object `x`, but all objects to which `x` has a reference are not copied, instead only references to these objects are stored. The `deepcopy(x)` function in turn copies the object `x` and makes copies (recursively) of all the objects that `x` refers to, which is called a deep copy.

To learn more about the `copy` module you can have a look at its
[official documentation](https://docs.python.org/3/library/copy.html).

## Wild West Game

The `game.py` file is based on the example of the same name from the abstract factory pattern, but has been simplified and contains only the Western theme. Direct instantiation of the `Weapon`, `Cowboy` and `Horse` classes is artificially implemented to simulate complex object creation.

The `Western` class in turn initializes an object of each type, and when we call its create method it returns a copy of the requested class instance, saving the processing time involved in the creation.

## Music21 Library

The [Music21](http://web.mit.edu/music21/) library is a set of tools developed for computer-aided musicological analysis. Creating copies of objects such as scores, notes, and pitches is performed when calling methods that make changes to the original content to preserve its state.

You can see some examples here:

[copy of `Score` object](https://github.com/cuthbertLab/music21/blob/747316f350319f0832d704c5d06a0c0bc2f07cbe/music21/variant.py#L232),

[copy of `Chord` object]( https://github.com/cuthbertLab/music21/blob/526bd3cea57aefaa855080d8870aa33bcf9f1ce4/music21/analysis/neoRiemannian.py#L35).

## Visualization ToolKit (VTK)

Another example of software that implements the Prototype pattern (_Prototype(xxx)_) is [VTK](https://vtk.org/) a set of tools for viewing and creating 3D images.

The creation of different graphic elements is done through the `newInstance` method (which returns a _Singleton_ prototitic instance) together with the `DeepCopy` method which copies the attributes of another instance used as a base.

[Here](https://github.com/Kitware/VTK/blob/8526db81234971bb2a36f12ee322b1b277841303/Rendering/Core/Testing/Python/cells.py#L62) you can see that the `aVoxel` instance is created and started naturally and then the `bVoxel` instance is made from the prototype and `aVoxel`.

<https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_prototype.htm>

<https://medium.com/design-patterns-in-python/prototype-design-pattern-in-python-45f8d3f15583>

<https://refactoring.guru/design-patterns/prototype/python/example>