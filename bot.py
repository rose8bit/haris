"""
bot.py
Created: May 29, 2020
"""

#importing modules...
"""
bot.py

created: May 29, 2020
"""

import discord
from discord.ext import commands
import os

bot = commands.Bot(
	command_prefix = "!", 
	description = "A bot to look for food deals.",
	owner_id=461656626567577630,
	case_insensitive=True)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

"""
cogs ------
greet.py - Greet new members.
"""
cogs = ['cogs.greet']
	
#bot startup
@bot.event
async def on_ready():
	print("=============")
	print("haris is ready!")
	
	#set "playing" status
	await bot.change_presence(activity = discord.Game(name = "beep boop"))
	
#Load cogs
if __name__ == "__main__":		
	#load cog files
	for cog in cogs:
		try:
			bot.load_extension(cog)
			print(f"Loaded cog '{cog}'")
		except Exception as err:
			exc = '{}: {}'.format(type(err).__name__, err)
			print('Failed to load cog {}\n{}'.format(cog, exc))	

bot.run(BOT_TOKEN)
