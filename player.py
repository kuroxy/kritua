import pygame


class Player:
    def __init__(self, startlocation, speed, animspeed):
        self.pos = pygame.Vector2(startlocation)
        self.speed = speed
        self.animspeed = animspeed
        self.collisionbox = pygame.Rect(self.pos, (8, 8))
        #   Player animations
        self.spr1 = pygame.image.load("entities\\player1.png")
        self.spr2 = pygame.image.load("entities\\player2.png")
        self.animcount = 0
        self.anim = 0

    def move(self, dt, keyinput):
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
        self.pos += dir * self.speed * dt
        self.collisionbox.x = self.pos.x
        self.collisionbox.y = self.pos.y

    def draw(self, surface, dt, camerapos):
        self.animcount += dt * self.animspeed
        if self.animcount > 1:
            self.animcount = 0
            self.anim += 1
            if self.anim > 1:
                self.anim = 0

        drawpos = self.collisionbox
        drawpos.x - camerapos[0]
        drawpos.y - camerapos[1]

        if self.anim == 0:
            surface.blit(self.spr1, drawpos)
        else:
            surface.blit(self.spr2, drawpos)
