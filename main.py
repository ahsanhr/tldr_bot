import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv
import os
import logging
import json
    # the stuff above are libraries to import that are useful for running the bot. 


intents = discord.Intents.default()
intents.message_content = True
intents.members = True
    # these are your intents that you toggled on or off in the discord dev portal. you have to toggle it on in there and THEN make it True in python.
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
server_id = os.getenv('DEVELOPER_SERVER_ID')
    # this is from the os library to make it easier
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
    # used at the .run command


class JSONHandler(commands.Converter):
    def __init__(self, sT, sD, eT, eD): #change these to have default parameters of 2 hours ago. done by sT=[2HoursAgo] eT =[currentTime]
        self.startTime = sT
        self.startDate = sD
        self.endTime = eT
        self. endDate = eD
    async def timeConvert(self, ctx, args):
        return

class Client(commands.Bot): 
    async def on_ready(self):
        print("its time")
            # example of how a function goes: 
            # @decorator and then.. 
            # define a function using async def [function name]: 
            # and then anything you want
        try:
            GUILD_ID = discord.Object(id=server_id)
            synced = await self.tree.sync(guild=GUILD_ID)
            print(f'Synced {len(synced)} commands to guild {GUILD_ID.id}')

        except Exception as e:
            print(f"error syncing commands {e}")

    async def on_message(self, message):
        if message.author == client.user:
            return
                # ok so this ensures that we dont get into an infinite loop in case something the bot says triggers this command again.

        await client.process_commands(self, message)
            # what this does is continue processing the rest of the commands in your python script. 
            # you use this line at the end when you have a on_message(message): function.
            
    # i probably wont need this command? but i shall see. 


client = Client(command_prefix = '!', intents=intents)
    # this is from discord.ext import commands, makes it easier to use the !prefix. 
GUILD_ID = discord.Object(id=server_id)
@client.tree.command(name="tldr", description="summarize the past 2 hours of messages!", guild=GUILD_ID)
    # this is for a / command in discord
async def tldr(interaction: discord.Interaction, hours: int):
    await interaction.response.send_message(hours)
        # what this is saying is that in this interaction send the message in the ()

@client.tree.command(name="help", description="use this command for instructions", guild=GUILD_ID)
async def help(interaction: discord.Interaction):
    embed = discord.Embed(title="TLDR Help", description="commands and their descriptions")
    embed.add_field(name="/tldr", value="summarize the past [#] hours of conversation!")
    await interaction.response.send_message(embed=embed)

client.run(token, log_handler=handler, log_level=logging.DEBUG)
        # the purpose of this is to run the bot accessing our token, and the log stuff eables logging inside discord.log file.