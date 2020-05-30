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
	command_prefix = "$", 
	descpription = "I look for food deals on the internet.",
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
	
	#load cog files
	for cog in cogs:
		bot.load_extension(cog)
		print(f"Loaded cog '{cog}'")
	return
	
	#set "playing" status
	await bot.change_presence(activity = discord.Game(name = "beep boop"))

bot.run(BOT_TOKEN)
