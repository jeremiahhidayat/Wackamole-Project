import pygame
import random
import math


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        initalized = False
        row,col = 0,0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            if initalized == False:
                screen.blit(mole_image, mole_image.get_rect(topleft=(col*32,row*32)))

            # Drawing the Grid
            for i in range(16):
                pygame.draw.line(screen, "black", ((0,32*(i))), ((640,32*(i))))
            for i in range(20):
                pygame.draw.line(screen, "black", ((32*(i)),0), ((32*(i),512)))
            
            # Moving the mole around
            if event.type == pygame.MOUSEBUTTONDOWN:
                initalized = True
                (x,y) = event.pos
                x /= 32
                y /= 32
                if math.floor(x) == col and math.floor(y) == row:
                    # Randomizing the position
                    row, col = random.randrange(0,16), random.randrange(0, 20)
                    screen.blit(mole_image, mole_image.get_rect(topleft=(col*32,row*32)))
            screen.blit(mole_image, mole_image.get_rect(topleft=(col*32,row*32)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
