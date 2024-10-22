import pygame

import assets
import configs
from objects.background import Background
from objects.bird import Bird
from objects.column import Column
from objects.floor import Floor
from objects.gameover_message import GameOverMessage
from objects.gamestart_message import GameStartMessage
from objects.score import Score

pygame.init()

screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))

pygame.display.set_caption("Flappy Bird Game")

img = pygame.image.load('assets/icons/red_bird.png')
pygame.display.set_icon(img)
