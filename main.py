# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player


def main():
    pygame.display.set_mode()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    #manage the fps
    clock = pygame.time.Clock()
    dt = 0

    #manage the game loop
    while 1 > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        screen.fill("black")
        player.draw(screen)
        player.update(dt)
        pygame.display.flip()        
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

