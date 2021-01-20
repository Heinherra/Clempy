import json
import discord

_json_user_data = {}
_json_global_data = {}

_user_data_file = "data\\data_user.json"
_global_data_file = "data\\data_global.json"

user_data = None

def _on_boot():
	global user_data
	
	_load_from_disk()
	user_data = UserData()

def _load_from_disk():
	print("Loading data from disk...")
	
	global _json_global_data,_json_user_data

	with open (_user_data_file) as json_file:
		_json_user_data = json.load(json_file)

	with open(_global_data_file) as json_file:
		_json_global_data = json.load(json_file)

def _save_to_disk():

	print("Saving user data...")
	with open(_user_data_file,"w") as outfile:
		json.dump(_json_user_data,outfile)
	
	print("Saving global data...")
	with open(_global_data_file,"w") as outfile:
		json.dump(_json_global_data,outfile)

def save_global(name,value):
	_json_global_data[name] = value

def load_global(name, default):
	try:
		return _json_global_data[name]
	except:
		_json_global_data[name] = default
		return default

def get_getter(name,default):
	return lambda _ : load_global(name,default)

class UserData():
	
	def save(self, name : str, user: discord.User, value):
		key = user.id
		if key not in _json_global_data: _json_user_data[key] = {}
		_json_user_data[key][name] = value
	
	def get_getter(self, name : str, default):
		return lambda user : self.load(name,user,default)
	
	def get_setter(self, name : str):
		return lambda user,value : self.save(name, user, value)

	def get_encapsulator(self, name : str, default):
		return Encapsulator( name,default )

	def load(self, name : str, user : discord.User , default):
		key = user.id
		
		if key not in _json_user_data: _json_user_data[key] = {}
		if name not in _json_user_data[key]: _json_user_data[key][name] = default
		return _json_user_data[key][name]


class Encapsulator():
	
	def __init__(self, name : str, default):
		self.getter = user_data.get_getter(name,default)
		self.setter = user_data.get_setter(name)
		self.default = default

	def set(self, user : discord.User ,value):
		self.setter(user,value)

	def get(self, user : discord.User):
		return self.getter(user)

_on_boot()

