import glob
import importlib as imp
import json
import argparse
import clempy
import saveload

modules = []
sep = "\\"
moduleNames = [f.replace("modules" + sep,"").replace(".py","") for f in glob.glob("modules"+sep+ "**"+ sep+ "*.py")]
tempNames = [name for name in moduleNames if not name.startswith("__") ]
moduleNames = tempNames
#moduleDictionary = {} 

for name in moduleNames:
	module = imp.import_module('modules.' + name.replace(sep,"."))
	modules.append(module)
	#moduleDictionary[module.__name__] = module
	print("Loaded module " + module.__name__ )

keys = {}

with open ('keys.json') as key_file:
	keys = json.load(key_file)

parser = argparse.ArgumentParser()
parser.add_argument("--key",type=str,help="Bot will start in either 'master' 'beta' or 'dump' mode. Default is 'beta'",default="beta")
args = parser.parse_args()

print("Trying to start bot in " + args.key + " mode...")

clempy.init_client(modules,keys[args.key])

