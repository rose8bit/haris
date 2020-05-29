"""
bot.py
Created: May 29, 2020
"""

#importing modules...
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = config.pre, descprption = config.des)

bot.run(config.bot_token)
