import discord
from discord.ext import commands


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Error Cog has been loaded\n-----")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        error = getattr(error, 'original', error)
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('***Böyle bi komut yok aslan parçası***')
            await ctx.message.add_reaction('⛔')
        elif isinstance(error, commands.CommandOnCooldown):
            guild = ctx.guild
            if not guild:
                await ctx.reinvoke()
            else:
                var1 = error.retry_after
                var2 = int(var1)
                await ctx.send(f'Bu komutu {var2} saniye sonra kullanabilirsin.',delete_after=1)
        elif isinstance(error, commands.MissingPermissions):
            poo = discord.Embed(description="Bu komutu kullanmaya yetkin yok, aptal", color=discord.Color.dark_red())
            await ctx.send(embed=poo)
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Yazman gereken bazı şeyleri unuttun sanki, he?")
        else:
            raise(error)


    
def setup(bot):
    bot.add_cog(Errors(bot))