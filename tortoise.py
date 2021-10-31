import turtle as py_turtle
import random


class Tortoise:
    def __init__(self,
                 display=None,
                 x=None,
                 y=None,
                 heading=None,
                 color=None,
                 shape='turtle'):
        if x is None:
            x = random.randint(-200, 200)
        if y is None:
            y = random.randint(-200, 200)
        if heading is None:
            heading = random.randint(0, 360)
        if color is None:
            color = (random.randint(0, 255),
                     random.randint(0, 255),
                     random.randint(0, 255))

        self._turtle = py_turtle.Turtle()
        self._turtle.penup()
        self._turtle.color(color)
        self._turtle.setposition(x, y)
        self._turtle.setheading(heading)
        self._turtle.pendown()

        self._display = display
        self.shape = shape

        self.setup()

    def setup(self):
        pass

    def __getattr__(self, name):
        if name not in self.__dict__:
            func = getattr(self._turtle, name)
        else:
            func = self.__dict__[name]
        return func

    def get_shape(self):
        return self._shape

    def set_shape(self, shape):
        self._shape = shape
        self._turtle.shape(self._shape)

    shape = property(fget=get_shape, fset=set_shape)

    def is_onscreen(self):
        screen = py_turtle.getscreen()
        window_width = screen.window_width()
        window_height = screen.window_height()

        return (-window_width * .5 <= self.xcor() <= window_width * .5
                and -window_height * .5 <= self.ycor() <= window_height * .5)
