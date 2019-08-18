from sprite import Sprite
import random
import numpy as np

class Rain(Sprite):
	def __init__(self, name, color=(3, 74, 236), drops=10, splash_colors={}, update_time=82, dims=(16, 16), zval=0):
		super().__init__(name, update_time, dims, zval)
		self.color = color
		self.num_drops = drops
		self.splash_colors = []

		self.drops = []

	def update(self):
		if len(self.drops) < self.num_drops:
			if random.random() < self.num_drops/self.height:
				self.drops.append([random.randint(0, self.width-1), 0])
		self.pixels = np.full((self.width, self.height, 3), -1)
		for drop in self.drops:
			drop_x, drop_y = drop
			if drop_y >= self.height:
				splash = [drop_x-1, drop_x+1]
				for pos in splash:
					if(pos > 15):
						pos = 15
					if(pos < 0):
						pos = 0
					self.pixels[pos, self.height-1] = self.color
				self.drops.remove(drop)
			else:
				self.pixels[drop_x, drop_y] = self.color
			drop[1] += 1