import discord #not mandatory

async def on_load():
	"""on_load() is called when the module is first loaded or when it is reloaded. This is the first method that is called for each module.
	"""
	pass	

async def on_start():
	"""on_start() is called after on_load when all the modules have been loaded
	"""
	pass

async def on_unload():
	"""on_unload() is called before a module is unloaded.
	"""
	pass

async def on_config():
	"""on_config() is called when a reconfigure command is run. 
	"""
	pass

async def on_message(message : discord.Message):
	"""on_message() is called every time a message comes through. Refer to discordpy docs for more info about the message class.
	"""
	if message.content == "ping":
		await message.channel.send("module pong")
	
