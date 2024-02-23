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


screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("green")
    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()