import saveload

lambdaDic = {}

def on_start():
	add_command("$save", saveload._save_to_disk )
	add_command("$load", saveload._load_from_disk)

def add_command(command,action):
	lambdaDic[command] = action
	
async def on_message(message):
	if message in lambdaDic:
		lambdaDic[message]()
