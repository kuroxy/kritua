import pygame
from player import Player

#   initialize pygame
pygame.init()


SCREENSIZE = (256, 192)
WINSIZE = [960, 720]
MAXFPS = 120
clock = pygame.time.Clock()
renDis = pygame.Surface(SCREENSIZE)
winDis = pygame.display.set_mode(WINSIZE)

# load SysFont
nums = []
for i in range(0, 10):
    nums.append(pygame.image.load(f"3x3font\\{i}.png"))

#   player
p1 = Player((30, 30), 10, 1.4)

#   main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    #       physics
    dt = clock.tick(MAXFPS) / 1000.0

    keys = pygame.key.get_pressed()

    p1.move(dt, keys)

    #       rendering
    renDis.fill((0, 0, 0))

    p1.draw(renDis, dt, (0, 0))
    #   render fps overlay
    fps = str(int(clock.get_fps()))
    for i in range(len(fps)):
        renDis.blit(nums[int(fps[i])], (i*6+5, 5))

    #       scale render size to window screen
    pygame.transform.scale(renDis, WINSIZE, winDis)
    pygame.display.flip()
