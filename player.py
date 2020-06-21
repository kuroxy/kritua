import pygame
from math import floor


class Player:
    def __init__(self, startlocation, speed, animspeed):
        self.pos = pygame.Vector2(startlocation)
        self.speed = speed
        self.animspeed = animspeed
        #   Player animations
        self.spr1 = pygame.image.load("entities\\player1.png")
        self.spr2 = pygame.image.load("entities\\player2.png")
        self.animcount = 0
        self.anim = 0

    def move(self, dt, keyinput, map):
        posch = self.movement(dt, keyinput)

        if self.checkcollisions(self.pos+posch, map) == 1:
            pos = self.pos+posch
            if posch.x > 0:
                self.pos.x = floor(pos[0]/8)-8
            elif posch.x < 0:
                self.pos.x = floor(pos[0]/8)+8
            
            if self.checkcollisions(self.pos+posch, map) == 1:
                if posch.y > 0:
                    self.pos.y = floor(pos[0]/8)-8
                elif posch.y < 0:
                    self.pos.y = floor(pos[0]/8)+8
        else:
            self.pos += posch

    def movement(self, dt, keyinput):
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
        return (dir * self.speed * dt)

    def checkcollisions(self, pos, map):
        chunkx = floor(floor(pos[0]/8)/25)
        chunky = floor(floor(pos[1]/8)/25)
        posx = floor(pos[0]/8) - chunkx*5
        posy = floor(pos[1]/8) - chunky*5
        if map[f"{chunkx}.{chunky}"][posx+posy*5] == 0:
            return 0
        elif map[f"{chunkx}.{chunky}"][posx+posy*5] == 1:
            print("colliding")
            return 1
        return 2

    def draw(self, surface, dt, camerapos):
        self.animcount += dt * self.animspeed
        if self.animcount > 1:
            self.animcount = 0
            self.anim += 1
            if self.anim > 1:
                self.anim = 0

        drawpos = self.pos
        drawpos.x - camerapos[0]
        drawpos.y - camerapos[1]

        if self.anim == 0:
            surface.blit(self.spr1, drawpos)
        else:
            surface.blit(self.spr2, drawpos)
