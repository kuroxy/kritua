import pygame
from player import Player

#   initialize pygame
pygame.init()


SCREENSIZE = (256, 192)
WINSIZE = [960, 720]

defaultfont = pygame.font.SysFont('Comic Sans MS', 30)
clock = pygame.time.Clock()
renDis = pygame.Surface(SCREENSIZE)
winDis = pygame.display.set_mode(WINSIZE)

#   init for dt calculations
t = pygame.time.get_ticks()
getTicksLastFrame = t
deltaTime = (t - getTicksLastFrame) / 1000.0

#   player
p1 = Player((30, 30), 10, 1.4)

#   main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #       physics
    t = pygame.time.get_ticks()
    dt = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    keys = pygame.key.get_pressed()
    p1.move(dt, keys)

    #       rendering
    renDis.fill((0, 0, 0))

    p1.draw(renDis, dt, (0, 0))
    #       scale render size to window screen
    pygame.transform.scale(renDis, WINSIZE, winDis)
    pygame.display.flip()
