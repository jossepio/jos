import discord
from discord.ext import commands

server = "https://discord.gg/cQtcDhh"
davet = 'https://discord.com/oauth2/authorize?client_id=719936787790823497&permissions=8&scope=bot'
member = discord.Member


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help Cog has been loaded\n-----")

    @commands.command(aliases=["yardım"])
    async def help(self, ctx):
        embed = discord.Embed(
            title="Komut Listesi", colour=discord.Colour.orange())
        embed.add_field(name=":hammer_pick: ***Moderasyon***",
                        value="`clear`,`ban`,`unban`,`kick`,`uyar`,`softban`", inline=False)
        embed.add_field(name=":tada: ***Eğlence***",
                        value="`slots`,`dalga`,`yazıtura`,`meme`,`şamar`,`yumruk`,`iq`,`sence`", inline=False)
        embed.add_field(name=":information_source: ***Bilgi***",
                        value="`info`,`avatar`,`userinfo`,`serverinfo`", inline=False)
        embed.add_field(name=":wrench: ***İşlevsel***",
                        value="`bigemoji`,`spotify`,`covid`,`wiki`,`insta`,`game`,`topla`,`çıkar`,`çarp`,`böl`", inline=False)
        embed.add_field(name=":space_invader:***Destek Sunucusu***",
                        value=f'[:space_invader: Davet!]({server})', inline=False)
        embed.add_field(name=":mailbox_with_mail: ***Sunucuna Ekle***",
                        value=f'[:e_mail: Link!]({davet})', inline=False)
        embed.set_footer(
            text="Detaylı bilgi almak için j!mod, j!eğlence, j!bilgi , j!işlevsel yazabilirsiniz.")
        await ctx.send(embed=embed)

    @ commands.command()
    async def mod(self, ctx):
        embed = discord.Embed(
            title=":hammer_pick: Moderasyon Komut Listesi", colour=discord.Colour.orange())
        embed.add_field(
            name="clear", value="Belirttiğiniz sayıda mesajı siler")
        embed.add_field(
            name="ban", value="Belirttiğiniz üyeyi sunucudan yasaklar")
        embed.add_field(
            name="unban", value="Belirttiğiniz üyenin yasaklamasını kaldırır")
        embed.add_field(
            name="kick", value="Belirttiğiniz üyeyi sunucudan atar")
        embed.add_field(
            name="uyar", value="Etiketlediğiniz kullanıcıyı uyarır.")
        embed.add_field(
            name="softban", value = "Etiketlediğiniz kullanıcıyı sunucudan yasaklar ardından yasaklamasını kaldırır. Gönderdiği mesajları silmek amacıyla kullanılır.")
        await ctx.send(embed=embed)

    @ commands.command()
    async def eğlence(self, ctx):
        embed = discord.Embed(title=":tada: Eğlence Komut Listesi",
                              colour=discord.Colour.orange())
        embed.add_field(
            name="slots", value="Slot oynamak için kolu çekersiniz.")
        embed.add_field(
            name="dalga", value="Malafat boyunuzu tahmin eden eğlenceli komut.")
        embed.add_field(name="yazıtura",
                        value="İddialı Yazı - Tura oynayabileceğiniz komut.")
        embed.add_field(
            name="meme", value="Reddit'ten en hit alan memeleri sunar.")
        embed.add_field(
            name="şamar", value="Belirttiğiniz kullanıcıya şamar atar")
        embed.add_field(
            name="yumruk", value="Belirttiğiniz kullanıcıya yumruk atar")
        embed.add_field(
            name="iq", value="IQ puanınızı tahmin etmeye çalışan eğlenceli komut")
        embed.add_field(
            name="sence", value="Soru sorup eğlenceli cevap alabieceğiniz komut")
        embed.add_field(
            name="gif", value="Belirttiğiniz türdeki gifleri sunan komut.")
        await ctx.send(embed=embed)

    @ commands.command()
    async def bilgi(self, ctx):
        embed = discord.Embed(title=":information_source: Bilgi Komut Listesi",
                              colour=discord.Colour.orange())
        embed.add_field(
            name="info", value="Botun kaç sunucuda kaç üyeye hizmet verdiğini, versiyonunu gösterir.")
        embed.add_field(
            name="avatar", value="Belirttiğiniz üyenin / sizin Discord profil resminizi atar.")
        embed.add_field(name="userinfo",
                        value="Belirttiğiniz kullanıcının bilgilerini sunar.")
        embed.add_field(name="serverinfo",
                        value="Bulunduğunuz sunucunun bilgilerini sunar.")
        await ctx.send(embed=embed)

    @ commands.command()
    async def işlevsel(self, ctx):
        embed = discord.Embed(title=":wrench: İşlevsel Komut Listesi",
                              colour=discord.Colour.orange())
        embed.add_field(name="bigemoji",
                        value="Seçtiğiniz emojinin büyük halini atar")
        embed.add_field(
            name="spotify", value="Belirttiğiniz kişinin / sizin spotify durumunuzu atar.")
        embed.add_field(
            name="covid", value="Belirttiğiniz ülke / kıta veya Dünyanın covid durumunu gösterir")
        embed.add_field(
            name="wiki", value="Belirttiğiniz şeyi Wikipedia'dan arayıp sonuç getirir.")
        embed.add_field(
            name="insta", value="Belirttiğiniz hesabın bilgilerini sunar.")
        embed.add_field(
            name="game", value="j!game yazıp ardından belirttiğiniz oyunu oynamak isteyen tüm üyelere duyurur.")
        embed.add_field(name="topla", value="Verdiğiniz iki sayıyı toplar")
        embed.add_field(
            name="çıkar", value="Verdiğiniz iki sayıya çıkartma işlemi yapar")
        embed.add_field(name="çarp", value="Verdiğiniz iki sayıyı çarpar")
        embed.add_field(
            name="böl", value="Verdiğiniz sayılara bölme işlemi uygular")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))