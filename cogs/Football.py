# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import soccer_data_api
from soccer_data_api import SoccerDataAPI
from classes.Leagues import Leagues

class Football(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def Table(self, ctx, *, league):
        try:
            #creating leagues object to get data about the needed league
            data = Leagues(league)

            embed = discord.Embed(title =league, description="League Table", color=discord.Colour.blue())
            embed.add_field(name="Teams", value="\n".join([team["team"]for team in data.get_league()]), inline=True)
            embed.add_field(name="Points", value="\n".join([team["points"]for team in data.get_league()]), inline=True)
            embed.add_field(name="Goal Difference", value="\n".join([team["goal_diff"]for team in data.get_league()]), inline=True)

            embed.set_image(url=data.get_logo())
            embed.set_footer(text='https://www.sports-reference.com/')
            await ctx.send(embed=embed)

        except (commands.BadArgument):
            await ctx.send("Available Leagues:" + "\t La Liga" + "\t Ligue 1" + "\t Premiere League" + "\t Bundesliga" + "\t Serie A" + "\t Eredivisie" + "\t Russian Premier League" + "\t English Championship")

    @commands.command()
    async def TopScorer(self, ctx, *, league):
        try:
            data = Leagues(league)
            top = data.get_top_scorer()
            embed = discord.Embed(title =league, description="", color=discord.Colour.blue())
            embed.add_field(name="Top Goal Scorer", value=top, inline=False)
            embed.set_footer(text='https://www.sports-reference.com/')
            await ctx.send(embed=embed)
        
        except (commands.BadArgument):
            await ctx.send("Available Leagues:" + "\t La Liga" + "\t Ligue 1" + "\t Premiere League" + "\t Bundesliga" + "\t Serie A" + "\t Eredivisie" + "\t Russian Premier League" + "\t English Championship")

        


def setup(client):
    client.add_cog(Football(client))
