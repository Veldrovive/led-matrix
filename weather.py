from landscape import Landscape
from sprite import FrameSprite

from time import sleep

volcano = FrameSprite("volcano", shift = (5, 0), num_frames=3, update_time=1000,
color_map = {
	"*": (105,105,105),
	"@": (255, 0, 0)
})
background = Landscape()
background.add_sprite(volcano)

while True:
	background.update()
	sleep(0.1)
