class FlyBehavior:
    """
    "Abstract" class for the fly strategy, not really
    necessary to create this class, since the python language has
    weak typing, and therefore it is also not necessary that the strategies
    inherit from that class. This was done here for didactic reasons.
    """
    def fly(self):
        raise NotImplementedError


class NotFly(FlyBehavior):
    """
    Class for the no-fly strategy.
    """
    def fly(self):
        print("I don't fly.")


class FlyWithWings(FlyBehavior):
    """
    Class for the Fly with wings strategy.
    """
    def fly(self):
        print("I'm flying!")


class QuackBehavior:
    """
    "Abstract" class for the quack strategy, not really
    necessary to create this class, since the python language has
    weak typing, and therefore it is also not necessary that the strategies
    inherit from that class. This was done here for didactic reasons.
    """
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    """
    Class for the quack strategy.
    """
    def quack(self):
        print("Quack")


class Squeak(QuackBehavior):
    """
    Class for the "squeak" strategy.
    """
    def quack(self):
        print("Squeak")


class NoSquaw(QuackBehavior):
    """
    Class for the no-quack strategy.
    """
    def quack(self):
        print("<< Silence... >>")


class Duck:
    """
    This class models the behaviors common to all duck types.
    """
    fly_behavior = None
    quack_behavior = None

    def __repr__(self):
        raise NotImplementedError

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, including baits")


class RoyalDuck(Duck):
    """
    Class that models a real duck. Real ducks fly and quack.
    """
    quacking_behavior = Quack()
    flying_behavior = FlyWithWings()

    def __repr__(self):
        return "I'm a real real duck"


class RubberDuck(Duck):
    """
    Class that models a rubber duck. ducks of
    rubber don't fly and "squeak", instead of
    quack
    """
    squawking_behavior = Squeak()
    flying_behavior = NotFly()

    def __repr__(self):
        return "I'm a rubber duck"


def main():
    """
    "Duck Simulator" from the book example.
    """
    mall_duck = RoyalDuck()
    print(mall_duck)
    mall_duck.quack()
    mall_duck.fly()

    rubber_duck = RubberDuck()
    print(rubber_duck)
    rubber_duck.quack()
    rubber_duck.fly()


if __name__ == '__main__':
    main()