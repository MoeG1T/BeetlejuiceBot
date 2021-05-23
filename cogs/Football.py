# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import soccer_data_api
from soccer_data_api import SoccerDataAPI


class Football(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.soccer_data = SoccerDataAPI()

    @commands.command()
    async def Table(self, ctx, *, league):
        try:
            # choosing league data based on user need
            data = []
            url = ""
            if(league == "Premiere League"):
                data = self.soccer_data.english_premier()
                url = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Premier_League_Logo.svg/1200px-Premier_League_Logo.svg.png"
            elif(league == "La Liga"):
                data = self.soccer_data.la_liga()
                url = "https://iscreativestudio.com/wp-content/uploads/2016/08/logotipos4.jpg"
            elif(league == "Ligue 1"):
                data = self.soccer_data.ligue_1()
                url = "https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Ligue_1_Uber_Eats.svg/1200px-Ligue_1_Uber_Eats.svg.png"
            elif(league == "Bundesliga"):
                data = self.soccer_data.bundesliga()
                url = "https://www.logofootball.net/wp-content/uploads/bundesliga-logo.png"
            elif(league == "Serie A"):
                data = self.soccer_data.serie_a()
                url = "https://www.insidesport.co/wp-content/uploads/2020/02/1581149078672.png"
            elif(league == "Eredivisie"):
                data = self.soccer_data.eredivisie()
                url = "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0f/Eredivisie_nieuw_logo_2017-.svg/1200px-Eredivisie_nieuw_logo_2017-.svg.png"
            elif(league == "Russian Premier League"):
                data = self.soccer_data.russian_premier()
                url = "https://europeanleagues.com/wp-content/uploads/RUS-PL-new.png"
            elif(league == "English Championship"):
                data = self.soccer_data.english_championship()
                url = "https://upload.wikimedia.org/wikipedia/en/3/37/EFL_Championship.png"

            embed = discord.Embed(title=league, description="League Table From Beetlejuice to You", color=discord.Colour.blue())
            embed.add_field(name="Teams", value="\n".join([team["team"]for team in data]), inline=True)
            embed.add_field(name="Points", value="\n".join([team["points"]for team in data]), inline=True)
            embed.add_field(name="Goal Difference", value="\n".join([team["goal_diff"]for team in data]), inline=True)

            embed.set_image(url=url)
            embed.set_footer(text='https://www.sports-reference.com/')
            await ctx.send(embed=embed)

        except:
            await ctx.send("Available Leagues:" + "\t La Liga" + "\t Ligue 1" + "\t Premiere League" + "\t Bundesliga" + "\t Serie A" + "\t Eredivisie" + "\t Russian Premier League" + "\t English Championship")

def setup(client):
    client.add_cog(Football(client))
