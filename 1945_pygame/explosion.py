from point import *
from renderer import *
class Explosion:
    def __init__(self):
        self.position = Point()
        paths = ["resources/explosions/{0}.png".format(i) for i in range(7)]
        self.renderer = loadAnimation(paths)
        self.active = True

    def run(self):
        if self.renderer.has_ended:
            self.active = False