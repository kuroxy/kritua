import pygame
import os
import json
from math import floor


class terrain(object):
    def __init__(self, tilepath, levelfolder):
        self.levelfolder = levelfolder
        self.tiles = []
        for n in range(len(os.listdir(tilepath))):
            try:
                tile = pygame.image.load(f"{tilepath}{n}.png").convert()
                self.tiles.append(tile)
            except Exception as e:
                raise e

        self.loadedtilemap = None
        self.loadedcollisionmap = None

    def loadlevel(self, levelname):
        f = open(f"{self.levelfolder}\\{levelname}.json", "r")
        self.loadedtilemap = json.loads(f.read())
        f.close()

        b = open(f"{self.levelfolder}\\col{levelname}.json", "r")
        self.loadedcollisionmap = json.loads(b.read())
        b.close()


    def drawchunk(self, surface, camerapos, windowsize):

        for chunk in self.loadedtilemap:
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

            for i in range(len(self.loadedtilemap[chunk])):
                dpos = [0, 0]
                dpos[0] = i % 5*8-camerapos[0]+pos[0]*40
                dpos[1] = floor(i/5)*8-camerapos[1]+pos[1]*40
                surface.blit(self.tiles[self.loadedtilemap[chunk][i]], dpos)

    def drawcollision(self, surface, camerapos, windowsize):
        for chunk in self.loadedcollisionmap:
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

            for i in range(len(self.loadedcollisionmap[chunk])):
                if self.loadedcollisionmap[chunk][i] == 1:
                    dpos = [0, 0]
                    dpos[0] = i % 5*8-camerapos[0]+pos[0]*40
                    dpos[1] = floor(i/5)*8-camerapos[1]+pos[1]*40

                    pygame.draw.rect(surface, (200, 0, 0), (dpos, (8, 8)))

    def createnewlevel(self):
        self.loadedtilemap = {}
        self.loadedcollisionmap = {}
        print("creating empty level")

    def savelevel(self, filename):
        print(f"level saved as {filename}")
        jsonfile = json.dumps(self.loadedtilemap)
        f = open(f"{self.levelfolder}\\{filename}.json", "w")
        f.write(jsonfile)
        f.close()

        jsonfile = json.dumps(self.loadedcollisionmap)
        f = open(f"{self.levelfolder}\\col{filename}.json", "w")
        f.write(jsonfile)
        f.close()

    def addtilechunk(self, strchunkpos):
        chunkstr = []
        print(f"added new tile chunk {strchunkpos}")
        for i in range(25):
            chunkstr.append(0)
        self.loadedtilemap[strchunkpos] = chunkstr

    def loadedcollisionchunk(self, strchunkpos):
        chunkstr = []
        print(f"added new collision chunk {strchunkpos}")
        for i in range(25):
            chunkstr.append(0)
        self.loadedcollisionmap[strchunkpos] = chunkstr

    def settile(self, tilepos, tiletype):
        chunkpos = f"{floor(tilepos[0]/5)}.{floor(tilepos[1]/5)}"

        if chunkpos not in self.loadedtilemap:
            self.addtilechunk(chunkpos)

        pos = tilepos[1] % 5 * 5 + tilepos[0] % 5
        self.loadedtilemap[chunkpos][pos] = tiletype

    def setcollision(self, tilepos, collisiontype):
        pass
        chunkpos = f"{floor(tilepos[0]/5)}.{floor(tilepos[1]/5)}"

        if chunkpos not in self.loadedcollisionmap:
            self.loadedcollisionchunk(chunkpos)

        pos = tilepos[1] % 5 * 5 + tilepos[0] % 5
        self.loadedcollisionmap[chunkpos][pos] = collisiontype

#       ter = terrain("tiles\\")
#   ter.createnewlevel()
#   ter.addtile((0, 0), 1)
#   ter.savelevel("levels\\testlv.json")
