import pygame
import os
import json


class terrain(object):
    def __init__(self, tilespath):
        self.tiles = []
        for filename in os.listdir(tilespath):
            self.tiles.append(pygame.image.load(f"{tilespath}{filename}"))

        self.loadedlevel = None
        self.loadedpos = (0, 0)

    def loadchunk(self, path, pos):
        self.loadedpos = pos
        f = open(path, "r")
        self.loadedlevel = json.loads(f.read())
        f.close()
        print(self.loadedlevel)

    def drawchunk(self, surface, camerapos, windowsize):
        if self.loadedpos[0]-camerapos[0] > windowsize[0]:
            return
        if self.loadedpos[1]-camerapos[1] > windowsize[1]:
            return

        for chunk in self.loadedlevel:
            pos = (chunk.split("."))
            pos[0] = int(pos[0])
            pos[1] = int(pos[1])
            if pos[0]+self.loadedpos[0]-camerapos[0]-25 > windowsize[0]:
                print("1")
                continue
            if pos[0]+self.loadedpos[0]-camerapos[0] < 0:
                print("2")
                continue

            if pos[1]+self.loadedpos[1]-camerapos[1]-25 > windowsize[1]:
                print("3")
                continue
            if pos[0]+self.loadedpos[1]-camerapos[1] < 0:
                print("4")
                continue

            for i in range(len(self.loadedlevel[chunk])):
                surface.blit(self.tiles[int(self.loadedlevel[chunk][i])], (i%5*8 - camerapos[0] + pos[0]*40, int(i/5)*8- camerapos[1] + pos[1]*40))
