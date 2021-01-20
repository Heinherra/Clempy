import discord
import traceback
import importlib as imp

modules = []

class Clempy(discord.Client):

	async def on_ready(self):
		print("Logged on as {0}!".format(self.user))
		
		for module in modules: 
			if hasattr(module,"on_load"): await module.on_load()
		
		for module in modules: 
			if hasattr(module,"on_start"): await module.start()

	async def on_message(self,message):
		if message.author == client.user:
			return
		
		for module in modules:
			try:
				if hasattr(module,"on_message"):
					await module.on_message(message)
			except Exception as e:
				print("[!] Module failed to receive message : " + module.__name__ )
				traceback.print_exc()


def reimport_index(moduleNumber):
	modules[moduleNumber] = reimport(modules[moduleNumber])

#def reimport_name(moduleName):
#	moduleDictionary[moduleName] = reimport(moduleDictionary[moduleName])

def reimport(module):
	if hasattr(module,"on_unload"): module.on_unload()
	return imp.reload(module)

def init_client(mods,key):
	global client,modules

	modules = mods
	client = Clempy()
	
	try:
		
		client.run(key)
	except:
		print("Couldn't start client with key")
		traceback.print_exc()


