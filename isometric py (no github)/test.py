import pygame,sys, random, math
from map import map
import time


displaySize = [1080,720]

pygame.init()
display = pygame.display.set_mode((displaySize[0], displaySize[1]))

tilesize = 2**8
print(tilesize)
grass = pygame.transform.scale(pygame.transform.rotate(pygame.transform.scale(pygame.image.load("grasstest.png").convert(),(tilesize,tilesize)),45), (tilesize,int(tilesize/2)))
# MAIN LOOP
while True:
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clearin screen
    display.fill((20,20,20))



    display.blit(grass, (100,100))



    pygame.display.flip()
