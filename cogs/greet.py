import discord
from discord.ext import commands

class Greetings(commands.Cog):
	def __init__(self, bot):
		self.client = bot
		self._last_member = None
		
	@commands.Cog.listener()
	async def on_member_join(self, member):
		welcomeMsg = "Welcome {0.mention}!"
		channel = member.guild.system_channel
		if channel is not None:
			await channel.send(welcomeMsg.format(member))
			
	@commands.command()
	async def welcomeMsg(self):
		await self.client.say(welcomeMsg)
		
def setup(bot):
	bot.add_cog(Greetings(bot))
