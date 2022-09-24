from turtle import Turtle, Screen
from PIL import Image
from io import BytesIO
from tkinter import filedialog

# Example of using the Strategy Pattern (Strategy)
#
# Here we have the Turtle class as context, which uses the Turtle class from
# Python to create a canvas where you can draw with the movement of the
# turtle, and different strategies to save the screen (each strategy generates
# a different file type)
#
# Keys for use:
# Up arrow: move the turtle forward
# Down arrow: move the turtle backwards
# Left arrow: rotate the turtle 45º counterclockwise
# Right arrow: rotate the turtle 45º clockwise
# Letter s: opens the menu to save the image.


class SaveScreen:
    """
    "Abstract" class for the rescue strategy, not really
    necessary to create this class, since the python language has
    weak typing, and therefore it is also not necessary that the strategies
    inherit from that class. This was done here for didactic reasons.
    """
    def save(self, file_name, screen):
        raise NotImplementedError


class SaveScreenPNG(SaveScreen):
    """
    Strategy for PNG files
    """
    def save(self, file_name: str, screen: Screen):
        image = BytesIO(screen.postscript(colormode='color').encode('utf-8'))
        Image.open(image).save(file_name, 'png')


class SaveScreenPDF(SaveScreen):
    """
    Strategy for PDF files
    """
    def save(self, file_name: str, screen: Screen):
        image = BytesIO(screen.postscript(colormode='color').encode('utf-8'))
        Image.open(image).save(file_name, 'pdf')


class SaveScreenJPG(SaveScreen):
    """
    Strategy for JPG files
    """
    def save(self, file_name: str, screen: Screen):
        image = BytesIO(screen.postscript(colormode='color').encode('utf-8'))
        Image.open(image).save(file_name, 'jpeg')


class SaveScreenEPS(SaveScreen):
    """
    Strategy for postscript files
    """
    def save(self, file_name: str, screen: Screen):
        screen.postscript(colormode='color', file=file_name)


# list of accepted types passed as a parameter
TYPES = (
    ('PDF Document', '*.pdf'),
    ('Image JPG', '*.jpg'),
    ('PNG image', '*.png'),
    ('PostScript file', '*.eps')
)


# Factory Method for the proper strategy
def select_strategy(file_name):
    format = file_name[-3:] # select the last 3 characters of the file_name
    strategies = {
        'pdf': SaveScreenPDF,
        'jpg': SaveScreenJPG,
        'png': SaveScreenPNG,
        'eps': SaveScreenEPS
    }
    return strategies[format]()


class Turtle():
    """
    Turtle Class

    Class responsible for generating the interactive graphical interface for the drawing
    and save it to file according to different strategies
    """

    def __init__(self, width: int = 500, height: int = 500):
        turtle = Turtle('turtle')
        self.screen = Screen()
        self.screen.setup(width, height)
        self.screen.onkey(lambda: turtle.forward(45), "Up")
        self.screen.onkey(lambda: turtle.left(45), "Left")
        self.screen.onkey(lambda: turtle.right(45), "Right")
        self.screen.onkey(lambda: turtle.back(45), "Down")
        self.screen.onkey(self.save, 's')
        self.screen.listen()
        self.screen.mainloop()

    def save(self):
        """
        Saves the screen where the drawing was performed according to the format of
        chosen file
        """
        file_name = filedialog.asksaveasfilename(filetypes=TYPES,
                                                    defaultextension='*.*')
        safe = select_strategy(file_name)
        safe.save(file_name, self.screen.getcanvas())


if __name__ == '__main__':
    Turtle()