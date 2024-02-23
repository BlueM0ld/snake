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


# snake position

snake_pos = pygame.Vector2(screen.get_width()/2, screen.get_height()/2)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("green")
    
    
    # Generates a bits on the screen
    # TODO: Randomly generate it on the screen
    food = pygame.Rect(screen.get_width()/2, screen.get_height()/2,10,10)
    pygame.draw.rect(screen, "red", food, 40)
    
    pygame.display.flip()
    clock.tick(60)
    
    
pygame.quit()