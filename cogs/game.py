import discord
from discord.ext import commands

class Game(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("Game Cog has been loaded\n-----")

    @commands.group(help="Base command")
    async def game(self,ctx):
        if ctx.invoked_subcommand is None:    
            await ctx.message.delete()
            await ctx.send("`Lütfen oynamak istediğiniz oyunu belirtin.`",delete_after=5)
    
    @game.group(help="PUBG oyuncularına duyuruluyor...")
    async def pubg(self,ctx,member= discord.Member):
        await ctx.send(f"Tamamdır {ctx.author.name}, PUBG oynamak istediğini tüm üyelere söylüyorum!\n@everyone bi bakalım buraya...")

    @game.group(help="LoL oyuncularına duyuruluyor...")
    async def lol(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, LoL oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')
    
    @game.group(help="Valorant oyuncularına duyuruluyor...")
    async def valorant(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Valorant oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="CS:GO oyuncularına duyuruluyor...")
    async def csgo(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, CS:GO oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Apex oyuncularına duyuruluyor...")
    async def apex(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Apex oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="RS6 oyuncularına duyuruluyor...",aliases=["rainbow"])
    async def rs6(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, RS6 oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="TFT oyuncularına duyuruluyor...")
    async def tft(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, TFT oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Minecraft oyuncularına duyuruluyor...",aliases=['mc'])
    async def minecraft(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Minecraft oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="COD: Warzone oyuncularına duyuruluyor...")
    async def warzone(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, COD: Warzone oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')
    
    @game.group(help="Raft oyuncularına duyuruluyor...")
    async def raft(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name},Raft oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="HOI oyuncularına duyuruluyor...",aliases=["hoi"])
    async def hoi4(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, HOI4 oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Roblox oyuncularına duyuruluyor...")
    async def roblox(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Roblox oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Rust oyuncularına duyuruluyor...")
    async def rust(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Rust oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="COD: Warzone oyuncularına duyuruluyor...",aliases=["gtav","gta5"])
    async def gta(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, GTA V oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Forest oyuncularına duyuruluyor...")
    async def forest(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Forest oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

    @game.group(help="Warcraft oyuncularına duyuruluyor...")
    async def warcraft(self,ctx,member=discord.Member):
        await ctx.send(f'Tamamdır {ctx.author.name}, Warcraft oynamak istediğini tüm üyelere söylüyorum\n@everyone bi bakalım buraya...')

def setup(client):
    client.add_cog(Game(client))