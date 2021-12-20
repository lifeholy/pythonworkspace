#Modified Minho,Lee 2020.12.27
import pygame
from inputmanager import *
from gamemanager import *
from player import *
from background import *
from constraints import *
from enemy import *

def init_pygame():
    pygame.init()
    screen = pygame.display.set_mode((400, 600)) # 600, 800 vs 768, 1024
    pygame.display.set_caption("Minho's 1945 Strikers - Remade by TechKidsers, leeminho")
    return screen

def run():
    game_manager.run()

def draw(screen):
    screen.fill((0, 0, 0))

    game_manager.draw(screen)

screen = init_pygame()
clock = pygame.time.Clock()

game_manager.add(Background())
player = Player()
player.constraints = Constraints(0, 400, 0, 600)

game_manager.add(player)

enemy = Enemy()
enemy.position.x = 200

game_manager.add(enemy)

loop = True

pygame.mixer.music.load("resources/sounds/bgm.mp3")
pygame.mixer.music.play(-1)



#spawner

while loop:
    events = pygame.event.get()

    # Handle QUIT event
    for event in events:
        if event.type == pygame.QUIT:
            loop = False

    input_manager.run(events)

    ## Update logic
    run()

    ## update graphics
    draw(screen)

    ## delay by frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()