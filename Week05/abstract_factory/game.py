# Theme Western Product Family
class Horse:
    def move(self):
        print("Pocotó, Pocotó, Pocotó...")


class Cowboy:
    def speak(self):
        print('Irraaa')


class Gun:
    def shoot(self):
        print('Pow!')


# Spatial Tem Product Family
class Ship:
    def move(self):
        print("Vshhhh")


class Pilot:
    def speak(self):
        print('Enable warp speed')


class LaserGun:
    def shoot(self):
        print('Pew! Pew!')


class Theme:
    """
    "Abstract" Factory class for creating concrete Factories
    """

    def create(self, item: str):
        """
        Returns a new object of type item according to the chosen theme
        """
        return self.items.get(item)()


class Western(Theme):
    def __init__(self):
        self.items = {
            'vehicle': Horse,
            'character': Cowboy,
            'gun': Gun
        }


class Space(Theme):
    def __init__(self):
        self.items = {
            'vehicle': Ship,
            'character': Pilot,
            'gun': LaserGun
        }


if __name__ == '__main__':
    # Create a list of all possible concrete Factories
    themes = [t.__name__ for t in Theme.__subclasses__()]
    # Create a menu to choose the Theme
    print('Choose game theme:')
    for i, t in enumerate(themes):
        print(f'{i}) {t}')
    theme = int(input('Theme : '))
    # Start the game with the chosen scenario
    scenario = Theme.__subclasses__()[theme]()
    vehicle = scenario.create('vehicle')
    character = scenario.create('character')
    gun = scenario.create('gun')
    # Use the items according to the chosen scenario
    gun.shoot()
    character.speak()
    vehicle.move()