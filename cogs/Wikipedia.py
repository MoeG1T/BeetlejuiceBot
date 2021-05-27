# Beetlejuice
# date 4/20/2021
# By Mohammed Fakhri

import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup


class Wikipedia(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def wikipedia_get(self, ctx):
        try:

            url_open = requests.get("https://en.wikipedia.org/wiki/Enzo_Ferrari")

            soup = BeautifulSoup(url_open.content, 'lxml')

            para = soup.find_all('p')
            #find the info box
            table = soup.find('table', class_='infobox biography vcard')
            data_rows = table.find_all('tr')
        
            header_value = {}
            for row in data_rows:
                #find all headers and values in a row
                value_tags = row.find_all('td', class_='infobox-data')
                header_tags = row.find_all('th', class_='infobox-label')
                #creates lists of headers and values in a row
                b_header = [header.text.strip() for header in header_tags]
                b_value = [value.text.strip() for value in value_tags ]
            
                if (len(b_value)  == 0):
                    continue

                for i in range(len(b_header)): 
                    dict[b_header[i]] = b_value[i]
            
            print("Hello")
            await ctx.send("lol")
        
        except:
            print("idk")
        

def setup(client):
    client.add_cog(Wikipedia(client))
