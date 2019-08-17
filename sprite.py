import numpy as np
import time
import os

class Sprite:
	def __init__(self, name, update_time=-1, dims=(16, 16), zval=0):
		self.name = name
		self.update_time = update_time
		self.dims = dims
		self.width, self.height = dims
		self.z = zval
		self.pixels = np.full((*dims, 3), -1)
		self.next = 0
		self.top_char, self.side_char, self.empty_char = "-", "|", "o"

	def init_update(self, curr_time=None):
		if self.update_time < 0:
			return
		if curr_time is None:
			curr_time = time.time()*1000
		if curr_time > self.next:
			self.next += self.update_time
			if(curr_time - self.next > self.update_time):
				self.next = curr_time + self.update_time
			self.update()
			return

	def update():
		# This function must update the values in self.pixels
		pass

	def get_pixel_val(self, x, y):
		if(self.pixels[x, y, 0] == -1):
			return None
		else:
			return self.pixels[x, y]


class FrameSprite(Sprite):
	def __init__(self, name, color_map={}, shift=(0, 0), num_frames=1, update_time=-1, dims=(16, 16), zval=0):
		super().__init__(name, update_time, dims, zval)
		self.frames = np.full((num_frames, *dims, 3), -1)
		self.num_frames = num_frames
		self.curr_frame = 0
		self.color_map = color_map
		self.x_shift, self.y_shift = shift
		self.gen_file(num_frames)
		self.read_file()
		self.update()

	def gen_file(self, frames=1):
		try:
			os.mkdir("./sprites")
		except FileExistsError:
			pass
		if not os.path.isfile("./sprites/{}.txt".format(self.name)):
			frame = ""
			frame += self.top_char*(self.width*3+2) + "\n"
			for i in range(self.height):
				frame += self.side_char+" {} ".format(self.empty_char)*self.width+self.side_char+"\n"
			frame += self.top_char*(self.width*3+2) + "\n\n"
			f = open("./sprites/{}.txt".format(self.name), "a")
			for i in range(frames):
				f.write(frame)

	def read_file(self):
		f = open("./sprites/{}.txt".format(self.name))
		frame_count = -1
		line_count = 0
		for line in f:
			if line[0] == self.top_char:
				if line_count < 1:
					frame_count += 1
				line_count = 0
			elif line[0] == self.side_char:
				chars = line.replace(self.side_char, "").replace(" ", "").strip()
				for i, char in enumerate(chars):
					try:
						color = self.color_map[char]
					except KeyError:
						color = (-1, -1, -1)
					x = i+self.x_shift
					y = line_count+self.y_shift
					if(x < self.width and x >= 0 and y < self.height and y >= 0):
						self.frames[frame_count, x, y] = color
				line_count += 1

	def update(self):
		self.pixels = self.frames[self.curr_frame]
		self.curr_frame = (self.curr_frame+1)%self.num_frames