import random
import turtle as py_turtle
from pathlib import Path
from tortoise import Tortoise
from utils import Display


TRACK_PATH = Path('track.gif')
MAX_MOVE = 10
NUMBER_OF_TURTLES = 5


class RaceTortoise(Tortoise):
    def move(self):
        dist = MAX_MOVE * random.random()
        self._turtle.forward(dist)

    def is_finished(self):
        if self.xcor() > 288:
            if not self.done:
                self.place_tortoise.write(self._display.get_place())
                self.done = True
            return True
        else:
            return False

    def setup(self):
        self.penup()
        self.place_tortoise = PlaceTortoise(x=320, y=self.ycor() - 8)
        self.done = False


class PlaceTortoise:
    def __init__(self, x=0, y=0):
        self._turtle = py_turtle.Turtle()
        self._turtle.hideturtle()
        self._turtle.penup()
        self._turtle.setposition(x, y)

    def write(self, text):
        self._turtle.write(text,
                           move=False,
                           font=('Arial', 12, 'normal'))


class RaceDisplay(Display):
    def setup(self):
        self.current_place = 0
        self.screen.bgpic(picname=str(TRACK_PATH))
        self.screen.title('The Great Race!')
        self.turtles = [RaceTortoise(x=-286,
                                     y=-40 + 20 * i,
                                     heading=0,
                                     display=self)
                        for i in range(NUMBER_OF_TURTLES)]
        self._count_down = 5
        self.countdown()

    def get_place(self):
        self.current_place += 1
        return self.current_place

    def run(self):
        self.setup()

    def countdown(self):
        if self._count_down > 0:
            self.screen.title(f'Race start in {self._count_down}')
            self._count_down = self._count_down - 1

            self.screen.ontimer(self.countdown, 1000)
        else:
            self.screen.title('GO!!!')
            self._run()

    def update(self):
        random.shuffle(self.turtles)
        for turtle in self.turtles:
            turtle.move()

        self.turtles = [turtle
                        for turtle in self.turtles
                        if not turtle.is_finished()]

        if not self.turtles:
            self.shutdown()

    def shutdown(self):
        super().shutdown()
        self.screen.title('All Done!')


def main():
    display = RaceDisplay(step_delay=10)
    display.run()
    display.screen.mainloop()


if __name__ == '__main__':
    main()
