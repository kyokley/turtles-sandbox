import random
from tortoise import Tortoise
from utils import Display


MAX_MOVE = 300
NUMBER_OF_TURTLES = 3
DRAW_STEPS = 60
REGENERATION_CHANCE = .25


class SpiralTortoise(Tortoise):
    def setup(self):
        rot_angle = random.randint(0, 360)
        self._turtle.left(rot_angle)

        self.draw_steps = DRAW_STEPS
        self.done = False

        self.rot_angle = random.randint(90, 270)
        self.dist = MAX_MOVE * random.random()

    def move(self):
        if self.draw_steps:
            self._turtle.left(self.rot_angle)
            self._turtle.forward(self.dist)
            self.draw_steps = self.draw_steps - 1
        else:
            self.hideturtle()
            self.done = True


class SpiralDisplay(Display):
    def setup(self):
        self.screen.title('Spirograph')
        self.turtles = []

    def update(self):
        if len(self.turtles) < NUMBER_OF_TURTLES:
            if random.random() < REGENERATION_CHANCE:
                self.turtles.append(SpiralTortoise(shape='arrow'))

        self.turtles = [turtle
                        for turtle in self.turtles
                        if not turtle.done]

        for turtle in self.turtles:
            turtle.move()


def main():
    display = SpiralDisplay(step_delay=5)
    display.run()

    display.screen.mainloop()


if __name__ == '__main__':
    main()
