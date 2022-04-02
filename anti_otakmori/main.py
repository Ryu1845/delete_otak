from os import getenv

import discord

client = discord.Client()
BANNED_CLIPPERS = {
    "otakmori": "UCF4-I8ZQL6Aa-iHfdz-B9KQ",
    "holoyume": "UC0zZ3QsUhYq6hQ0A-_THfgA",
    "iroha": "UCizN2tVLNcwP67bAHlVRg1Q",
    "fuwamomo": "UCmd-9kqE3VGMYCqiUy7QnWw",
    "yaku": "UCegRyiPSOfnUiCQ3lTLhsYQ",
    "kami": "KamiClips",
}


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return

    embed: discord.Embed
    for embed in message.embeds:
        if any(
            channel_id in embed.author.url for channel_id in BANNED_CLIPPERS.values()
        ):
            await message.delete()


client.run(getenv("TOKEN"))