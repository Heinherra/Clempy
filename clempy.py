import discord

class Clempy(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))

    async def on_message(self,message):

        if message.author == self.user:
            return

        if(message.content == "ping"):
            await message.channel.send("pong")

client = Clempy()
client.run("NTY3MjI3NDU1Mzg0MDU5OTA0.XLQduw.2SnMpTmtIWhC1bwE1qoIc6ycG4c")


