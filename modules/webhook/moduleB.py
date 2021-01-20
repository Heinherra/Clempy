

async def on_message(message):
	if message.content == "pingB":
		await message.channel.send("ponging from B")

