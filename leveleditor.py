import pygame
import sys
from math import floor
from terrain import terrain

#   initialize pygame
pygame.init()

SCREENSIZE = (256, 192)
WINSIZE = [960, 720]
SCALING = [WINSIZE[0]/SCREENSIZE[0], WINSIZE[1]/SCREENSIZE[1]]
MAXFPS = 100000

renDis = pygame.Surface(SCREENSIZE)
winDis = pygame.display.set_mode(WINSIZE)

pygame.display.set_caption("Kritua leveleditor")
clock = pygame.time.Clock()

averagefps = None

# load SysFont
nums = []
for i in range(0, 10):
    nums.append(pygame.image.load(f"5x5font\\{i}.png"))

#   camera
cameraposfloat = [0, 0]
camerapos = [int(cameraposfloat[0]), int(cameraposfloat[1])]


def cameramovement(keyinput, cameraposfloat, dt):
    dir = pygame.Vector2(0, 0)
    #   userinput
    if keyinput[pygame.K_w]:
        dir.y -= 1
    if keyinput[pygame.K_s]:
        dir.y += 1
    if keyinput[pygame.K_a]:
        dir.x -= 1
    if keyinput[pygame.K_d]:
        dir.x += 1

    if dir != (0, 0):
        dir.normalize_ip()
    # change pos of player and collisionbox
    cameraposfloat[0] += dir[0] * 30 * dt
    cameraposfloat[1] += dir[1] * 30 * dt
    return cameraposfloat


#   Terrain
ter = terrain("tiles\\")
ter.createnewlevel()
#   ter.loadlevel("levels\\lv1.json", (0, 0))

#   leveleditor
selectedtile = 0

skeyup = False
okeyup = False


#   main loop
while True:
    skeyup = False
    okeyup = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(f"averagefps = {averagefps}")
            pygame.quit()
            sys.exit()

        # change selectedtile
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                selectedtile -= 1
                if selectedtile < 0:
                    selectedtile = len(ter.tiles)-1
                print(f"selectedtile : {selectedtile}")

            if event.button == 5:
                selectedtile += 1
                if selectedtile >= len(ter.tiles):
                    selectedtile = 0
                print(f"selectedtile : {selectedtile}")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                skeyup = True
            if event.key == pygame.K_o:
                okeyup = True

    #       physics
    dt = clock.tick(MAXFPS) / 1000.0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LCTRL]:
        if skeyup:
            print("Saving level as (path\\\\filename \".json\")")
            name = input()
            if name:
                ter.savelevel(name)
        if okeyup:
            print("opening level (path\\\\filename \".json\")")
            name = input()
            if name:
                ter.loadlevel(name)
    else:
        cameraposfloat = cameramovement(keys, cameraposfloat, dt)
        camerapos = [int(cameraposfloat[0]), int(cameraposfloat[1])]

    #   mouse events
    mousebuttons = pygame.mouse.get_pressed()

    #   mouse down draw tile on that location
    if mousebuttons[0]:
        mousepos = pygame.mouse.get_pos()
        posx = floor((mousepos[0]/SCALING[0] + camerapos[0])/8)
        posy = floor((mousepos[1]/SCALING[1] + camerapos[1])/8)
        ter.settile((posx, posy), selectedtile)

    #   rendering
    renDis.fill((0, 0, 0))

    ter.drawchunk(renDis, camerapos, SCREENSIZE)

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
