from renderer import *
from boxcollider import *
from physics import *

class Enemy:
    def __init__(self):
        self.position = Point()
        self.renderer = loadAnimation(["resources/enemies/yellow/0.png", "resources/enemies/yellow/1.png", "resources/enemies/yellow/2.png"])
        self.active = True
        self.box_collider = BoxCollider(self.position, 28, 30)
        physics.add(self)

    def run(self):
        self.position.add_up(0, 1)