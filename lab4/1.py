import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (255, 0, 0), (120, 165), 40)
circle(screen, (0, 0, 0), (120, 165), 40, 1)
circle(screen, (0, 0, 0), (120, 165), 10)
circle(screen, (255, 0, 0), (280, 165), 30)
circle(screen, (0, 0, 0), (280, 165), 30, 1)
circle(screen, (0, 0, 0), (280, 165), 10)
line(screen, (0,0,0), (120,280), (280,280),40)
line(screen, (0,0,0), (70,70), (175,160), 30)
line(screen, (0,0,0), (230,160), (330,100), 30)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
