import noise
import numpy as np
import time




class map():
    def __init__(self, seed, mapsize, scale):
        self.shape = mapsize
        self.scale = scale
        self.octaves = 10
        self.persistence = 0.5
        self.lacunarity = 2.0
        self.seed = seed


    def get_map(self, pos):
        time1= time.time()
        world = np.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                world[i][j] = (noise.pnoise2((i+pos[0])/self.scale + self.seed,
                                            (j+pos[1])/self.scale + self.seed,
                                            octaves=self.octaves,
                                            persistence=self.persistence,
                                            lacunarity=self.lacunarity,
                                            )+.5)
        print(f"It took {time.time()-time1} sec")
        return world
