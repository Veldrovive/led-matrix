from landscape import Landscape
from sprite import FrameSprite

from time import sleep

from Client import Client

client = Client("weather-led", "https://central-socket.herokuapp.com/")

volcano = FrameSprite("volcano", shift = (5, 0), num_frames=3, update_time=1000,
color_map = {
	"*": (105,105,105),
	"@": (255, 0, 0)
})
background = Landscape()

def onWeatherChange(weather):
	if(isinstance(weather, list)):
		weather = weather[0]
	if(weather == 'hot'):
		background.add_sprite(volcano)
	else:
		background.remove_sprite(volcano)
	print("New weather: {}".format(weather))

client.on("weatherChange", onWeatherChange)

while True:
	background.update()
	sleep(0.1)
