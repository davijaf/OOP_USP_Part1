from copy import deepcopy
from time import sleep, time


# Family of Western-themed Products
class Horse:
    def __init__(self):
        sleep(1) # simulate a complex computation for object creation

    def move(self):
        print("Pocotó, Pocotó, Pocotó...")


class Cowboy:
    def __init__(self):
        sleep(1.5) # simulate a complex computation for object creation

    def speak(self):
        print('Irraaa')


class Revolver:
    def __init__(self):
        sleep(0.25) # simulate a complex computation for object creation

    def shoot(self):
        print('Pow!')


class Western:
    def __init__(self):
        self.items = {
            'horse': Horse(),
            'cowboy': Cowboy(),
            'weapon': Revolver()
        }

    def create(self, item):
        return deepcopy(self.items[item])


if __name__ == '__main__':
    # Start the game with the chosen scenario
    print("Starting Element Factory:", end=' ')
    start = time()
    scenery = Western()
    print(f'It took {time() - start:.2f} seconds')

    print('Creating a Cowboy')
    start = time()
    cowboy1 = scenery.create('cowboy')
    print(f'It took {time() - start} seconds')

    print('Creating another Cowboy')
    start = time()
    cowboy2 = scenery.create('cowboy')
    print(f'It took {time() - start} seconds')
    print('Modifying the cowboys to see they are different instances')
    cowboy1.name = 'Bad'
    cowboy2.name = 'Ugly'
    print(f'Cowboy 1 calls: {cowboy1.name} and cowboy 2: {cowboy2.name}.')