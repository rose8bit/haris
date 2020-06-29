"""
streamer_role.py

created: June 27, 2020

Features:
- Give members the "LIVE" role when they start streaming if they have the "STREAMER" role
- Remove the "LIVE" role from members when they stop streaming, if they have the "STREAMER" role

Commands:

"""

import discord
from discord.ext import commands

class Streamer_role(commands.Cog):
	def __init__(self, bot):
		self.client = bot
		
	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		print('{} before activity type: {}'.format(before.display_name, str(before.activities)))
		print('{} after activity type: {}\n'.format(after.display_name, after.activity.type.name))
def setup(bot):
	bot.add_cog(Streamer_role(bot))
