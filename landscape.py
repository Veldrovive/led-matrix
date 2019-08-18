import numpy as np
try:
    import unicornhathd as unicorn
    print("unicorn hat hd detected")
    real_unicorn = True
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn
    real_unicorn = False

class Landscape:
	def __init__(self, background=(135, 206, 235)):
		self.width, self.height = unicorn.get_shape()
		self.sprites = []
		self.background = background
		self.test = not real_unicorn

	def add_sprite(self, sprite):
		self.sprites.append(sprite)

	def remove_sprite(self, sprite):
		try:
			self.sprites.remove(sprite)
			return True
		except ValueError:
			return False

	def update(self):
		for sprite in self.sprites:
			sprite.init_update()
		for x in range(self.width):
			true_x = self.width-1-x
			for y in range(self.height):
				unicorn.set_pixel(true_x, y, *self.background)
				currZ = None
				for sprite in self.sprites:
					if(currZ is None or sprite.z >= currZ):
						pixel = sprite.get_pixel_val(x, y)
						if(pixel is not None):
							unicorn.set_pixel(true_x, y, *pixel)
							currZ = sprite.z
		unicorn.show()


