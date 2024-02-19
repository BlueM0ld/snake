import pygame
import random

# set up the board

WIDTH = 600
HEIGHT = 600
BITS = 30

pygame.font.init()
score_font = pygame.font.SysFont("times new roman", 20)
score=0

#colour

WHITE = (255, 255,255)
RED = (255, 0 , 0)

pygame.init()


win = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()