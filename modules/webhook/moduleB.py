try:
	instance
except NameError:
		instance = None

client = None

async def on_load(c):
	global client
	client = c

async def on_message(message):
	if message.author != client.user:
		await message.channel.send("ponging from B")

