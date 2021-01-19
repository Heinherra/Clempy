import discord
import glob
import importlib as imp
import json
import sys
import argparse

modules = []
sep = "\\"
moduleNames = [f.replace("modules" + sep,"").replace(".py","") for f in glob.glob("modules"+sep+ "**"+ sep+ "*.py")]
tempNames = [name for name in moduleNames if not name.startswith("__") ]
moduleNames = tempNames
moduleDictionary = {} 

for name in moduleNames:
	module = imp.import_module('modules.' + name.replace(sep,"."))
	modules.append(module)
	moduleDictionary[module.__name__] = module
	print("Loaded module " + module.__name__ )

def reimport_index(moduleNumber):
	modules[moduleNumber] = reimport(modules[moduleNumber])

def reimport_name(moduleName):
	moduleDictionary[moduleName] = reimport(moduleDictionary[moduleName])

def reimport(module):
	if hasattr(module,"on_unload"): module.on_unload()
	return imp.reload(module)

class Clempy(discord.Client):

	async def on_ready(self):
		print("Logged on as {0}!".format(self.user))
	
		for module in modules: 
			if hasattr(module,"on_load"): await module.on_load(self)
		
		for module in modules: 
			if hasattr(module,"start"): await module.start()

	async def on_message(self,message):
		for module in modules:
			try:
				if hasattr(module,"on_message"):
					await module.on_message(message)
			except:
				print("Module failed to receive message : " + module.__name__ ) #get module name'


keys = {}

with open ('keys.json') as key_file:
	keys = json.load(key_file)

parser = argparse.ArgumentParser()

parser.add_argument("--key",type=str,help="Bot will start in either 'master' 'beta' or 'dump' mode. Default is 'beta'",default="beta")
args = parser.parse_args()

client = Clempy()

try:
	print("Trying to start bot in " + args.key + " mode...")
	client.run(keys[args.key])
except:
	print("Couldn't start client with key")


