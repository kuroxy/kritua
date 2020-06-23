import pygame
from math import floor


class Player:
    def __init__(self, startlocation, speed, animspeed):
        self.pos = pygame.Vector2(startlocation)
        self.speed = speed
        self.movecooldown = 0
        #   Player animations
        self.spr1 = pygame.image.load("entities\\player1.png")
        self.spr2 = pygame.image.load("entities\\player2.png")

    def move(self, keyinput, map):
        dir = self.movement(keyinput)
        print(dir)
        newpos = self.pos+dir
        chunkx = floor(newpos.x/5)
        chunky = floor(newpos.y/5)
        x = newpos.x - chunkx*5
        y = newpos.y - chunky*5
        if map[f"{chunkx}.{chunky}"][int(y*5+x)] == 0:
            self.pos = newpos
        #    ifnot it is colliding

    def movement(self, event):
        dir = pygame.Vector2(0, 0)
        if self.movecooldown <= 0:
            if event.key == pygame.K_w:
                dir.y = -1
            if event.key == pygame.K_s:
                dir.y = 1
            if event.key == pygame.K_a:
                dir.x = -1
            if event.key == pygame.K_d:
                dir.x = 1

        if dir != [0, 0]:
            self.movecooldown = self.speed
        print(self.movecooldown)
        return dir

    def cooldown(self, dt):
        self.movecooldown -= dt

    def draw(self, surface, dt, camerapos):
        drawpos = self.pos*8
        drawpos.x - camerapos[0]
        drawpos.y - camerapos[1]

        #   if self.anim == 0:
        surface.blit(self.spr1, drawpos)
        #   else:
        #    surface.blit(self.spr2, drawpos)
