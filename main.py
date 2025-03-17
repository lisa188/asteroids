# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    # initialize the pygame module
    pygame.init()
    # set new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    refresh_rate = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        pygame.display.flip()
        
        # limit to 60 FPS
        dt = refresh_rate.tick(60) / 1000

if __name__ == "__main__":
    main()