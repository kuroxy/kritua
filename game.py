import pygame
import sys
from player import Player
from terrain import terrain


#   initialize pygame
pygame.init()

SCREENSIZE = (256, 192)
WINSIZE = [960, 720]
MAXFPS = 100000

renDis = pygame.Surface(SCREENSIZE)
winDis = pygame.display.set_mode(WINSIZE)

pygame.display.set_caption("Kritua")
clock = pygame.time.Clock()

averagefps = None

# load SysFont
nums = []
for i in range(0, 10):
    nums.append(pygame.image.load(f"5x5font\\{i}.png"))
#   camera
camerapos = [0, 0]

#   player
p1 = Player((10, 10), .1, 1.4)

#   Terrain
ter = terrain("tiles\\", "levels")
ter.loadlevel("tjeerd")


#   main loop
while True:
    dt = clock.tick(MAXFPS) / 1000.0
    p1.cooldown(dt)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"averagefps = {averagefps}")
            pygame.quit()
            sys.exit()
            #       physics
        if event.type == pygame.KEYDOWN:
            p1.move(event, ter.loadedcollisionmap)

    #       rendering
    renDis.fill((0, 0, 0))

    ter.drawchunk(renDis, camerapos, SCREENSIZE)

    p1.draw(renDis, dt, camerapos)
    #   render fps overlay
    fps = clock.get_fps()
    if fps != 0:
        if averagefps is None:
            averagefps = fps
        averagefps = (averagefps+fps)/2

    fps = str(int(fps))

    for i in range(len(fps)):
        renDis.blit(nums[int(fps[i])], (i*6+5, 5))

    #       scale render size to window screen
    pygame.transform.scale(renDis, WINSIZE, winDis)
    pygame.display.flip()
