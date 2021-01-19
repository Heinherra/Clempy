client = None



async def on_load(c):
	global client
	client = c

async def on_config():
	pass

async def on_unload():
	pass

async def start():
	pass

async def on_message(message):
	
	if message.author == client.user:
		return

	if message.content == "ping":
		await message.channel.send("module pong")
	
