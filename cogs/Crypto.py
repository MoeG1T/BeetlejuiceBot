# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import requests
import os

class Crypto(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.Token = os.environ.get('MARKET_KEY')
        self.url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"

    @commands.command()
    async def Top10(self, ctx):
        try: 

            headers = {
                            "X-CMC_PRO_API_KEY": self.Token,
                            "Accepts": "application/json"
                        }
            params = {
                            "start": "1",
                            "limit": "10", 
                            "convert": "USD"
                    }
        
            json = requests.get(self.url, params=params, headers=headers).json()
        
            embed = discord.Embed(title = "Cryptocurrency Market", description="Top 10 Crypto Coins", color=discord.Colour.dark_gold())
            #lists the top 10 coins
            embed.add_field(name="Name", value="\n".join(["\n" + str(i+1) + " - " + json["data"][i]["symbol"]  for i in range(len(json["data"]))]), inline=False)

            await ctx.send(embed = embed)

        except Exception as e:
            print(e)

    @commands.command()
    async def Coin(self, ctx, symbol):
        try: 

            headers = {
                            "X-CMC_PRO_API_KEY": self.Token,
                            "Accepts": "application/json"
                        }
            params = {
                            "start": "1",
                            "limit": "200", 
                            "convert": "USD"
                    }
        
            json = requests.get(self.url, params=params, headers=headers).json()
            
            valid = False
            change = 0
            marketCap = 0
            #finds the coin with the given symbol and then stores relative info
            for coin in json['data']:
                if symbol.upper() == coin['symbol']:
                    valid = True
                    change = coin['quote']['USD']["percent_change_24h"]
                    marketCap = coin['quote']['USD']["market_cap"]
                    price = coin['quote']['USD']["price"]
            
            if valid:
                embed = discord.Embed(title = "Cryptocurrency Market", description="Coin Info", color=discord.Colour.dark_gold())
                embed.add_field(name="Name", value=symbol.upper(), inline=False)
                embed.add_field(name="Price", value=price, inline=False)
                embed.add_field(name="24h Change", value=change, inline=False)
                embed.add_field(name="Market Cap", value=marketCap, inline=False)
    
                await ctx.send(embed = embed)
            
            else:
                await ctx.send("Invalid coin symbol. Check !Top50 for the available coins.")

        except Exception as e:
            print(e)

def setup(client):
    client.add_cog(Crypto(client))