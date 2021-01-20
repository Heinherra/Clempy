#import sys
#from modules.webhook import moduleB as B
import saveload
from saveload import user_data


pings_get = user_data.get_getter("pings",0)
pings_set = user_data.get_setter("pings")

pings = user_data.get_encapsulator("pings",0)

async def on_message(message):
	
	if message.content == "pingA":
		pings.set(message.author , pings.get(message.author) + 1)
		await message.channel.send("ponging from A")

	if message.content == "pings?":
		await message.channel.send("You pinged " + str(pings.get(message.author)) + "times" )
	
	if message.content == "save":
		saveload._save_to_disk()
