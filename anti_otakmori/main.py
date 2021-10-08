from os import getenv

import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    embed: discord.Embed
    for embed in message.embeds:
        if (
            embed.author.url
            == "https://www.youtube.com/channel/UCF4-I8ZQL6Aa-iHfdz-B9KQ"
        ):
            await message.delete()


client.run(getenv("TOKEN"))
