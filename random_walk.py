import random
from tortoise import Tortoise
from utils import Display


MAX_MOVE = 10
NUMBER_OF_TURTLES = 20
REGENERATION_CHANCE = .25


class RandomTortoise(Tortoise):
    def setup(self):
        self.pensize(5)
        self._can_move = True

        self._turtle.onclick(self.click)
        self._turtle.ondrag(self.drag)
        self._turtle.onrelease(self.release)

    def move(self):
        if self._can_move:
            if random.random() < .25:
                rot_angle = random.randint(-90, 90)
                self._turtle.left(rot_angle)

            dist = MAX_MOVE * random.random()
            self._turtle.forward(dist)

    def click(self, x, y):
        # print(f'click {x} {y}')
        self._can_move = False
        self._display.pause_updates()
        self.penup()

    def drag(self, x, y):
        # print(f'drag {x} {y}')
        self.setposition(x, y)

    def release(self, x, y):
        # print(f'release {x} {y}')
        self._can_move = True
        self._display.start_updates()
        self.pendown()


class RandomDisplay(Display):
    def setup(self):
        self.screen.title('Random Walk')
        self.turtles = [RandomTortoise(display=self)
                        for i in range(NUMBER_OF_TURTLES)]

    def update(self):
        if len(self.turtles) < NUMBER_OF_TURTLES:
            if random.random() < REGENERATION_CHANCE:
                self.turtles.append(RandomTortoise(display=self))

        for turtle in self.turtles:
            turtle.move()

        self.turtles = [turtle
                        for turtle in self.turtles
                        if turtle.is_onscreen()]


def main():
    display = RandomDisplay(step_delay=10)
    display.run()

    display.screen.mainloop()


if __name__ == '__main__':
    main()
