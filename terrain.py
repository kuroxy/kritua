import pygame
import os
import json
from math import floor


class terrain(object):
    def __init__(self, path):
        self.tiles = []
        for n in range(len(os.listdir(path))):
            try:
                self.tiles.append(pygame.image.load(f"{path}{n}.png").convert())
            except Exception as e:
                raise e

        self.loadedlevel = None
        self.levelcollision = None

    def loadlevel(self, levelpath):
        f = open(levelpath, "r")
        self.loadedlevel = json.loads(f.read())
        f.close()

# TODO: levelcollision

    def drawchunk(self, surface, camerapos, windowsize):

        for chunk in self.loadedlevel:
            pos = (chunk.split("."))
            pos[0] = floor(float(pos[0]))
            pos[1] = floor(float(pos[1]))
            if pos[0]*40 - camerapos[0] > windowsize[0]:
                continue
            if pos[0]*40 - camerapos[0] + 40 < 0:
                continue

            if pos[1]*40 - camerapos[1] > windowsize[1]:
                continue
            if pos[1]*40 - camerapos[1] + 40 < 0:
                continue

            for i in range(len(self.loadedlevel[chunk])):
                dpos = [0, 0]
                dpos[0] = i % 5*8-camerapos[0]+pos[0]*40
                dpos[1] = floor(i/5)*8-camerapos[1]+pos[1]*40
                surface.blit(self.tiles[self.loadedlevel[chunk][i]], dpos)

    def createnewlevel(self):
        self.loadedlevel = {}
        print("creating empty level")

    def savelevel(self, filename):
        print(f"level saved as {filename}")
        jsonfile = json.dumps(self.loadedlevel)
        f = open(f"{filename}", "w")
        f.write(jsonfile)
        f.close()

    def addchunk(self, strchunkpos):
        chunkstr = []
        print(f"added new chunk {strchunkpos}")
        for i in range(25):
            chunkstr.append(0)
        self.loadedlevel[strchunkpos] = chunkstr

    def settile(self, tilepos, tiletype):
        chunkpos = f"{floor(tilepos[0]/5)}.{floor(tilepos[1]/5)}"

        if chunkpos not in self.loadedlevel:
            self.addchunk(chunkpos)

        pos = tilepos[1] % 5 * 5 + tilepos[0] % 5
        self.loadedlevel[chunkpos][pos] = tiletype

#       ter = terrain("tiles\\")
#   ter.createnewlevel()
#   ter.addtile((0, 0), 1)
#   ter.savelevel("levels\\testlv.json")
