"""
bot.py
Created: May 29, 2020
"""

#importing modules...
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix = "$", descpription = "I look for food deals on the internet.")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
	
#bot startup
@bot.event
async def on_ready():
	print("=============")
	print("haris is ready!")
	
	#set "playing" status
	await bot.change_presence(activity = discord.Game(name = "beep boop"))

bot.run(BOT_TOKEN)
