# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot
from mine import Mine

def main():
    # initialize the pygame module
    pygame.init()
    # set new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    refresh_rate = pygame.time.Clock()

    #groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    mines = pygame.sprite.Group()

    #moving containers
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    Mine.containers = (mines, updateable, drawable)

    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    #player
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updateable.update(dt)

        for asteroid in asteroids: 
            if asteroid.collides_with(player):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()
            for mine in mines:
                if asteroid.collides_with(mine):
                    asteroid.split()
                    mine.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        # limit to 60 FPS
        dt = refresh_rate.tick(60) / 1000        

if __name__ == "__main__":
    main()