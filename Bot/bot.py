"""
bot.py
Created: May 29, 2020
"""

#importing modules...
import discord
from discord.ext import commands
import os

#config.py setup
if not os.path.isfile("config.py"):
	print("config.py not found")
else:
	print("config.py found! importing...")
	import config
	
#bot startup
@bot.event
async def on_ready():
	print("=============")
	print("haris is ready!")
	
	#set "playing" status
	await bot.change_presence(activity = discord.Game(name = "beep boop"))

bot = commands.Bot(command_prefix = config.pre, descprption = config.des)

bot.run(config.bot_token)
