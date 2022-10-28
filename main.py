import logging as log
from random import randint
import color
import pygame

HEIGHT = 480
WIDTH =  600
SIZE = (WIDTH, HEIGHT)
CAPTION = 'Yet Another pygqs Game'
FPS = 60

def main():
    log.basicConfig(level=log.INFO)

    pygame.init()
    pygame.display.set_caption(CAPTION)
    CANVAS = pygame.display.set_mode(SIZE)

    endOfGame = False
    clock = pygame.time.Clock()

    while not endOfGame:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log.info('The game loop will exit.')
                endOfGame = True

            CANVAS.fill(color.GRAY)

            # Here code the game do
            # E.g. To create an amusement where input makes a circle pulsate...
            pygame.draw.circle(CANVAS, color.PURPLE, (WIDTH / 2, HEIGHT / 2), randint(50,100), 1)
            pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
