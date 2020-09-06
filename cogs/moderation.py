import discord
from discord.ext import commands
from discord.utils import get
import re
import asyncio

reklamlar = ['https', 'http', '.com', '.gg', '.net', '.org']


class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Moderation Cog has been loaded\n-----")

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)

        embed = discord.Embed(
            title=f"{ctx.author.name}, {member.name} adlı kullanıcıyı kickledi!", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)

        embed = discord.Embed(
            title=f"{ctx.author.name}, {member.name} adlı kullanıcıyı banladı!", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        embed = discord.Embed(
            title=f"{ctx.author.name}, {member.name} adlı kullanıcının banını kaldırdı.", description=reason)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        deleted = await ctx.channel.purge(limit=amount)
        await ctx.channel.purge(limit=amount)
        await ctx.send(f"***{len(deleted)} mesaj silindi***", delete_after=5)

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def softban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=None)
        await member.unban()
        await ctx.send(f'{member.mention} softbanlandı.')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def uyar(self, ctx, member: discord.Member, *, reason=None):
        if ctx.author.top_role.position < member.top_role.position:
            await ctx.send("Bu kullanıcıyı uyarmak için gerekli yetkiye sahip değilsin.")
            return
        if ctx.author.id != ctx.guild.owner.id:
            await ctx.send("Sunucu sahibini uyaramazsın.")
            return
        if ctx.author == member:
            await ctx.send("Kendini uyaramazsın.")
            return
        else:
            e = discord.Embed(
                color=0x420000,
                title=f"⚠️ **{ctx.guild} sunucusunda uyarıldın!**\n__*Uyaran Admin*__:\n{ctx.author}\n__*Gerekçe*__:\n{reason}")
            await member.send(embed=e)
            await ctx.message.add_reaction(':white_check_mark:')


def setup(bot):
    bot.add_cog(Moderation(bot))