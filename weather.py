from landscape import Landscape
from sprite import FrameSprite
from Rain import Rain
from Client import Client
from time import sleep

volcano = FrameSprite("volcano", shift = (5, 0), num_frames=3, update_time=1000,
color_map = {
	"*": (105,105,105),
	"@": (255, 0, 0)
})
rain = Rain("rain", zval=100)
background = Landscape()

name = "weather-led-test" if background.test else "weather-led"
client = Client(name, "https://central-socket.herokuapp.com/")

def onWeatherChange(weather):
	if(isinstance(weather, list)):
		weather = weather[0]
	if weather == 'hot':
		background.add_sprite(volcano)
	elif weather == 'cold':
		background.remove_sprite(volcano)

	if weather == 'rainy':
		background.add_sprite(rain)
	elif weather == 'dry':
		background.remove_sprite(rain)
	print("New weather: {}".format(weather))

client.on("weatherChange", onWeatherChange)

while True:
	background.update()
	sleep(0.001)
