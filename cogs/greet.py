"""
greet.py

created: May 29, 2020

Features:
- welcomes new members

Commands:
"""

import discord
from discord.ext import commands

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.client = bot		
		
	@commands.Cog.listener()
	async def on_member_join(self, member):
		#welcomeMsg = "Welcome {0.mention}!"
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send(welcomeMsg.format(member))			
		
def setup(bot):
	bot.add_cog(Greetings(bot))
