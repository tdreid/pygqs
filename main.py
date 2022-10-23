import logging as log
from random import randint
import color
import pygame

log.basicConfig(level=log.INFO)

HEIGHT = 480
WIDTH =  600
SIZE = (WIDTH, HEIGHT)

pygame.init()
canvas = pygame.display.set_mode(SIZE)

endOfGame = False

while not endOfGame:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            log.info('The game loop will exit.')
            endOfGame = True

        canvas.fill(color.gray)

        # Here code the game do
        # E.g. To create an amusement where input makes a circle pulsate...
        # pygame.draw.circle(canvas, color.purple, (WIDTH / 2, HEIGHT / 2), randint(50,100), 1)

        pygame.display.flip()

pygame.quit()
