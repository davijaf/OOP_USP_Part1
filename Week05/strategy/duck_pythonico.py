# Example of the Strategy Pattern (Strategy) adapted from the book
# "Head First Design Patterns"
#

class NoFly:
    def fly(self):
        print("I don't fly.")


class FlyWithWings:
    def fly(self):
        print("I'm flying!")


class Quack:
    def quack(self):
        print("Quack")


class Squeak:
    def quack(self):
        print("Squeak")


class SquawMute:
    def quack(self):
        print("<< Silence... >>")


class Duck:
    """
    This class models the behaviors common to all duck types.
    """
    def __repr__(self):
        raise NotImplementedError

    def swim(self):
        print("All ducks float, including baits")


class RoyalDuck(Duck, Quack, FlyWithWings):
    """
    Class that models a real duck. Real ducks fly and quack.
    """
    def __repr__(self):
        return "I'm a real real duck"


class RubberDuck(Duck, Squeak, NoFly):
    """
    Class that models a rubber duck. ducks of
    rubber don't fly and "squeak", instead of
    quack
    """
    def __repr__(self):
        return "I'm a rubber duck"


if __name__ == '__main__':
    mall_duck = RoyalDuck()
    print(mall_duck)
    mall_duck.quack()
    mall_duck.fly()

    rubber_duck = RubberDuck()
    print(rubber_duck)
    rubber_duck.quack()
    rubber_duck.fly()