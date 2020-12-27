from inputmanager import *
from playerbullet import *
from point import *
from renderer import *

class Player:
    def __init__(self):
        self.position = Point()
        self.renderer = SpriteRenderer(pygame.image.load("resources/player.png"))

        self.cool_down_period = 10
        self.cool_down_counter = 0
        self.shoot_disabled = False

        self.constraints = None
        self.active = True
        self.position.y = 500
        self.position.x = 200

        self.shoot_sound = pygame.mixer.Sound("resources/sounds/shoot.wav")

    def run(self):
        self.move()
        self.shoot()

    def move(self):
        if input_manager.right_pressed:
            self.position.add_up(5, 0)
        if input_manager.left_pressed:
            self.position.add_up(-5, 0)
        if input_manager.down_pressed:
            self.position.add_up(0, 5)
        if input_manager.up_pressed:
            self.position.add_up(0, -5)

        if self.constraints is not None:
            self.constraints.make(self.position)

    def shoot(self):
        if self.shoot_disabled:
            self.cool_down_counter += 1
            if self.cool_down_counter >= 10:
                self.shoot_disabled = False
                self.cool_down_counter = 0
            return

        if input_manager.space_pressed:
            self.shoot_sound.stop()
            self.shoot_sound.play()
            player_bullet = PlayerBullet()
            player_bullet.position.copy(self.position.add(0, -10))
            game_manager.add(player_bullet)
            self.shoot_disabled = True