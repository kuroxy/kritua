import pygame,sys, random, math
from map import map
import time

terrain = map(0,(25,25), 20)


def renderisotile(surface, tile, pos, tilesize, camerapos):
    x = (pos[0]*.5*tilesize)-(pos[1]*.5*tilesize)
    y = (pos[0]*.25*tilesize)+(pos[1]*.25*tilesize) - (pos[2]*tilesize)/2
    surface.blit(tile,(int(x-camerapos[0]),int(y-camerapos[1])))

def genz(z):
    return math.floor(z*50-10)

def min(a,b):
    return a if a < b else b


campos = (-1080/2,-720/2)


cap = 20

# pygame settings

displaySize = [1080,720]

pygame.init()
display = pygame.display.set_mode((displaySize[0], displaySize[1]))

tilewidth = 32

tiles = []
tiles.append(pygame.transform.scale(pygame.image.load("tiles\\long.png").convert_alpha(), (tilewidth,tilewidth*10)))
tiles.append(pygame.transform.scale(pygame.image.load("tiles\\Isometric-Blocks_24.png").convert_alpha(), (tilewidth,tilewidth)))


clock = pygame.time.Clock()

move = 0


# MAIN LOOP
while True:
    # pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clearin screen
    display.fill((20,20,20))

    print(clock.get_fps())
    dt = 1/clock.tick(60)

    # draw screen
    currterrain = terrain.get_map((int(move),0))

    time1 = time.time()
    for y in range(len(currterrain)):
        for x in range(len(currterrain[y])):
            z = genz(currterrain[y][x])
            if z < cap:
                continue
            renderisotile(display, tiles[0], (x,y,z-1), tilewidth, campos)
    print(f"draw : it took {time.time()-time1} sec")
    move+=.1
    #update display
    pygame.display.flip()
