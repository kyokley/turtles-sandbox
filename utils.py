import turtle as py_turtle


class Display:
    def __init__(self, step_delay=250):
        py_turtle.colormode(255)
        # py_turtle.delay(10)
        py_turtle.onscreenclick(self.trigger_shutdown, btn=2)
        # py_turtle.onscreenclick(self.debug, add=True)
        py_turtle.hideturtle()
        self.step_delay = step_delay

        self._done = False
        self._can_update = True
        self.screen = py_turtle.getscreen()

    def debug(self, x, y):
        print(x, y)

    def setup(self):
        pass

    def run(self):
        self.setup()

        self._run()

    def _run(self):
        if self._done:
            py_turtle.exitonclick()
        elif self._can_update:
            self.update()
            self.screen.ontimer(self._run, self.step_delay)

    def update(self):
        pass

    def pause_updates(self):
        self._can_update = False

    def start_updates(self):
        self._can_update = True
        self.screen.ontimer(self._run, self.step_delay)

    def trigger_shutdown(self, x, y):
        if self._done:
            py_turtle.bye()
        else:
            self.shutdown()

    def shutdown(self):
        self._done = True
