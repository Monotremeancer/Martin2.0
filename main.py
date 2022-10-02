import os

import nextcord
from dotenv import load_dotenv
import beingMartin
client = nextcord.Client()

load_dotenv() #

TOKEN = os.getenv('DISCORD_TOKEN')

@client.slash_command(
    name="hello",
    description="A simple hello command.",
    guild_ids=[]
)
async def hello(inter: nextcord.Interaction) -> None:
    await inter.response.send_message("Hello!")


@client.slash_command(
    name="dinner",
    description="What should you eat for dinner.",
    guild_ids=[]
)
async def dinner(inter: nextcord.Interaction) -> None:
    await inter.response.send_message(beingMartin.whatToEat())


if __name__ == '__main__':
    client.run(TOKEN)