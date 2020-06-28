"""
streamer_role.py

created: June 27, 2020

Features:
- Give members the "LIVE" role when they start streaming if they have the "STREAMER" role
- Remove the "LIVE" role from members when they stop straeming, if they have the "STREAMER" role

Commands:

"""

import discord
from discord.ext import commands

class Streamer_role(commands.Cog):
	def __init__(self, bot):
		self.client = bot
		

def setup(bot):
	bot.add_Cog(Streamer_role(bot))
