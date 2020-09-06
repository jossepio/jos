import discord
from discord.ext import commands
from pathlib import Path # For paths
import random
import asyncio
from aiohttp import ClientSession
import aiohttp




class Covid(commands.Cog):
    """
    Covid API Commands!
    """



    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Covid Cog has been loaded\n-----")

    @commands.group(help= 'Base command')
    async def covid(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Lütfen geçerli bir komut kullanın: `All`, `Ülke`, `Kıta`")


    @covid.group(help= 'Ülkenin Covid-19 durumu hakkındaki bilgileri alıyor...')
    async def ülke(self, ctx, country1):
        url = f'https://disease.sh/v3/covid-19/countries/{country1}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                html = await response.json()
                data = [html]

                #getting data from API then format to readable numbers
                test = data[0]["countryInfo"]["flag"]
                population = data[0]["population"]
                population_format = format(population, ",")
                country = data[0]["country"]
                cases = data[0]["cases"]
                cases_format = format(cases, ",")
                deaths = data[0]["deaths"]
                deaths_format = format(deaths, ",")
                active = data[0]["active"]
                active_format = format(active, ",")
                recovered = data[0]["recovered"]
                recovered_format = format(recovered, ",")
                critical = data[0]["critical"]
                critical_format = format(critical, ",")
                tests = data[0]["tests"]
                tests_format = format(tests, ",")


                #making stats
                fatality = deaths/cases*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = cases/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/cases*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'{country} Covid Detayları')
                embed.set_thumbnail(url=test)
                embed.add_field(name='Toplam Vaka', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Toplam Ölüm', value=deaths_format, inline=True)
                embed.add_field(name='Aktif Hasta', value=active_format, inline=True)
                embed.add_field(name='İyileşen', value=recovered_format, inline=True)
                embed.add_field(name='Kritik', value=critical_format, inline=True)
                embed.add_field(name='Test', value=tests_format, inline=True)
                embed.add_field(name='Nüfus', value=population_format, inline=True)
                embed.add_field(name='Hasta Yüzdesi', value=infected_rate_percent, inline=True)
                embed.add_field(name='Ölü Yüzdesi', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Kritik Yüzdesi', value=critical_rate_percent, inline=True)
                embed.add_field(name='İyileşen Yüzdesi', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Yüzdesi', value=test_rate_percent, inline=True)
                await ctx.send(embed=embed)

    @covid.group(help= 'Tüm ülkelerin durumlarının özetleri alınıyor...')
    async def all(self, ctx):
        url = f'https://disease.sh/v3/covid-19/all'
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                #getting data from API then format to readable numbers
                case = data['cases']
                cases_format = format(case, ",")

                population = data["population"]
                population_format = format(population, ",")

                deaths = data["deaths"]
                deaths_format = format(deaths, ",")

                active = data["active"]
                active_format = format(active, ",")

                recovered = data["recovered"]
                recovered_format = format(recovered, ",")

                critical = data["critical"]
                critical_format = format(critical, ",")

                tests = data["tests"]
                tests_format = format(tests, ",")

                infected_countries = data['affectedCountries']


               


                #making stats
                fatality = deaths/case*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = case/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/case*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'Tüm Ülkelerin Covid Durumu')
                embed.set_thumbnail(url='https://i2x.ai/wp-content/uploads/2018/01/flag-global.jpg')
                embed.add_field(name='Toplam Vaka', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Toplam Ölüm', value=deaths_format, inline=True)
                embed.add_field(name='Aktif Hasta', value=active_format, inline=True)
                embed.add_field(name='İyileşen', value=recovered_format, inline=True)
                embed.add_field(name='Kritik', value=critical_format, inline=True)
                embed.add_field(name='Test', value=tests_format, inline=True)
                embed.add_field(name='Nüfus', value=population_format, inline=True)
                embed.add_field(name='Hasta Yüzdesi', value=infected_rate_percent, inline=True)
                embed.add_field(name='Ölü Yüzdesi', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Kritik Yüzdesi', value=critical_rate_percent, inline=True)
                embed.add_field(name='İyileşen Yüzdesi', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Yüzdesi', value=test_rate_percent, inline=True)
                await ctx.send(embed=embed)

    @covid.group(help= 'Kıtanın Covid-19 hakkındaki bilgileri alınıyor...')
    async def kıta(self, ctx, continent):
        url = f'https://disease.sh/v3/covid-19/continents/{continent}'
        async with ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()

                #getting data from API then format to readable numbers
                case = data['cases']
                cases_format = format(case, ",")

                population = data["population"]
                population_format = format(population, ",")

                deaths = data["deaths"]
                deaths_format = format(deaths, ",")

                active = data["active"]
                active_format = format(active, ",")

                recovered = data["recovered"]
                recovered_format = format(recovered, ",")

                critical = data["critical"]
                critical_format = format(critical, ",")

                tests = data["tests"]
                tests_format = format(tests, ",")

                countries = data['countries']


                #making stats
                fatality = deaths/case*100
                fatality_rounded_value = round(fatality, 4)
                fatality_rate_percent = "{}%".format(fatality_rounded_value)

                infected = case/population*100
                infected_format = round(infected, 4)
                infected_rate_percent = "{}%".format(infected_format)

                critical_rate = critical/active*100
                critical_rate_round = round(critical_rate, 4)
                critical_rate_percent = "{}%".format(critical_rate_round)


                recovered_rate = recovered/case*100
                recovered_rate_format = round(recovered_rate, 4)
                recovered_rate_percent = "{}%".format(recovered_rate_format)

                test_rate = tests/population*100
                test_rate_format = round(test_rate, 4)
                test_rate_percent = "{}%".format(test_rate_format)


                # making embed
                embed = discord.Embed(title=f'{continent} kıtasının Covid durumu')
                embed.set_thumbnail(url='https://i2x.ai/wp-content/uploads/2018/01/flag-global.jpg')
                embed.set_thumbnail(url='https://i2x.ai/wp-content/uploads/2018/01/flag-global.jpg')
                embed.add_field(name='Toplam Vaka', value=cases_format + '\u200b', inline=True)
                embed.add_field(name='Toplam Ölüm', value=deaths_format, inline=True)
                embed.add_field(name='Aktif Hasta', value=active_format, inline=True)
                embed.add_field(name='İyileşen', value=recovered_format, inline=True)
                embed.add_field(name='Kritik', value=critical_format, inline=True)
                embed.add_field(name='Test', value=tests_format, inline=True)
                embed.add_field(name='Nüfus', value=population_format, inline=True)
                embed.add_field(name='Hasta Yüzdesi', value=infected_rate_percent, inline=True)
                embed.add_field(name='Ölü Yüzdesi', value=fatality_rate_percent, inline=True)
                embed.add_field(name='Kritik Yüzdesi', value=critical_rate_percent, inline=True)
                embed.add_field(name='İyileşen Yüzdesi', value=recovered_rate_percent, inline=True)
                embed.add_field(name='Test Yüzdesi', value=test_rate_percent, inline=True)

                await ctx.send(embed=embed)




def setup(client):
    client.add_cog(Covid(client))