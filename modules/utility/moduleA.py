#import sys
#from modules.webhook import moduleB as B
client = None

async def on_load(c):
	global client
	client = c

async def on_message(message):
	if message.author != client.user:
		await message.channel.send("ponging from A")

