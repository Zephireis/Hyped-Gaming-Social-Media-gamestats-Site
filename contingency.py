import random
import discord
import asyncio
import aiohttp
import json
import asyncio
import sqlite3
import mysql.connector
import operator

from datetime import datetime
from discord import Game
from bs4 import BeautifulSoup
from discord.ext.commands import Bot




async def get_data():
    async with aiohttp.ClientSession()as session:
        url = "https://forum.project-contingency.com/index.php"
        response = await session.get(f'https://statcore01.pcon.statrepo.com/api/players/Zephireis')
        resp_json = await response.json() # coverting the data into json
        print(resp_json)
