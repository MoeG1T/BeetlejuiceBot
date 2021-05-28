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

    def get_info(self, data_rows):
        header_value = {}
        for row in data_rows:
            sub_table = [sub_row.text.strip() for sub_row in row.find_all('table')]
            #dismisses sub tables
            if(len(sub_table) != 0):
                continue

            #find all headers and values in a row
            value_tags = row.find_all('td')
            header_tags = row.find_all('th')
            #creates lists of headers and values in a row
            b_header = [header.text.strip() for header in header_tags]
            b_value = [value.text.strip() for value in value_tags ]
            
            if (len(b_value)  == 0):
                continue

            for i in range(len(b_header)): 
                header_value[b_header[i]] = b_value[i]
        
        return header_value
    
    @commands.command()
    async def wikipedia(self, ctx, *, url):
        url = url.replace(" ", "_")
        url_open = requests.get("https://en.wikipedia.org/wiki/" + url)

        soup = BeautifulSoup(url_open.content, 'lxml')

        #try finding the info box with this class
        table = soup.find('table', class_='infobox biography vcard')
        #Change class name if the table has not been found
        if(table is None):
            table = soup.find('table', class_='infobox vcard')
        #another table class possibility
        if(table is None):
            table = soup.find('table', class_='infobox vevent')

        if(table is None):
            table = soup.find('table', class_='infobox vcard plainlist')
            
        data_rows = table.find_all('tr')
            
        info = self.get_info(data_rows)
            
        for key, value in info.items():
            await  ctx.send(key + ' : \t' + value)
        

def setup(client):
    client.add_cog(Wikipedia(client))
