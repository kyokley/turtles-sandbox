import random
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
        return self.xcor() > 288

    def setup(self):
        self.penup()


class RaceDisplay(Display):
    def setup(self):
        self.screen.bgpic(picname=str(TRACK_PATH))
        self.turtles = [RaceTortoise(x=-286,
                                     y=-26 + 15 * i,
                                     heading=0)
                        for i in range(NUMBER_OF_TURTLES)]
        self._count_down = 5
        self.countdown()

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


def main():
    display = RaceDisplay(step_delay=10)
    display.run()
    display.screen.mainloop()


if __name__ == '__main__':
    main()
