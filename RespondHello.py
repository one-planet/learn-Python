import discord

client = discord.Client()

@client.event
async def on_message(message):
if message.author == client.user:
return
await client.send_message(message.channel, "Hello World")

