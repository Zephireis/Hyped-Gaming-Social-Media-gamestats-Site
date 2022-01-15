import asyncio
import requests
import env_vars
import databaseconnection
import aiohttp
import discord

from config import CLIENT_SECRET, TOKEN, OAUTH_URL, REDIRECT_URI
from flask import Flask, render_template, redirect, url_for, request, flash, Response, session
from zenora import APIClient
from contingency import get_data
from threading import Thread
from functools import partial
from discord.ext import commands
from env_vars import db_user, db_passwd, db_database, db_host
from databaseconnection import creds





app = Flask(__name__)
app.config["SECRET_KEY"] = "verysecret"
client = APIClient(TOKEN, client_secret=CLIENT_SECRET)
bot = commands.Bot(command_prefix="!")

@app.route('/')
def home():
    if 'token' in session:
        bearer_client = APIClient(session.get('token'), bearer=True)
        current_user = bearer_client.users.get_current_user()
        response = requests.get(f'https://statcore01.pcon.statrepo.com/api/players/{current_user.username}')
        gamedata=response.json()
        words = ["Games", "Won", "Lost", "Draw", "Kills", "Assists", "Deaths", "Suicides", "Betrayals"]
        statslist = []
        for i in range(8):
            data = words[i] # iterating thru the words by numnber index
            try:
                record = gamedata["Summary"][data] # player stats using the words from the word list
            except:
                record = "none"
            statsSummary = str(data) + ":" + " " + str(record)
            statslist.append(statsSummary)
        connection = creds(db_host, db_user, db_passwd, db_database)
        mycursor = connection.cursor()
        mycursor.execute("SELECT * FROM members")
        myresult = mycursor.fetchall()
        a = (myresult)

        return render_template("index.html", current_user=current_user, len = len(statslist), statslist=statslist, a=a )
    return render_template('index.html', oauth_uri=OAUTH_URL)


@bot.command(pass_context=True)
async def roles(ctx):
    rolelist = ['Division Leader', 'Squad leader', 'Squad Private']
    authorname = ctx.message.author.name
    roles = ctx.message.author.roles
    role_names = []
    for role in roles:
        role_names.append(role.name)
    # print(role_names)
    for i in range(3):
        data = rolelist[i]
        if data in role_names:
            a = rolelist.index(data) #method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found.
            print(rolelist[a])






    #rolestr = (str(roles))
    # word = rolestr.split(" ")
    # print(word)
    #
    # # if 'Division leader' in rolestr:
    # #     print(rolestr.find('Division leader'))
    # for i in range(3):
    #     data = word[i]
    #     if data in word:
    #         a = word.find(data)
    #         print(a)
    #         # print(rolestr[83])




@app.route("/oauth/callback")
def callback():
    code= request.args['code']
    access_token = client.oauth.get_access_token(code, REDIRECT_URI).access_token
    session['token'] = access_token
    return redirect("/") # redirecting to homepage

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@bot.command(pass_context=True)
async def register(ctx):
    authorid = ctx.message.author.id #discord user id
    authorname = ctx.message.author.name
    print(authorname)
    print(authorid)
    connection = creds(db_host, db_user, db_passwd, db_database)
    mycursor = connection.cursor()
    sql = "INSERT INTO members (discord_id, discord_name) VALUES (%s, %s)"
    val = (f"{authorid}", f"{authorname}")
    mycursor.execute(sql, val)
    connection.commit()










# medaldict = dict(decendingMedalOrder)
# for key in medaldict:
#     keylist.append(key)
# topMedals = ""
# for i in range(8):
#     data = keylist[i]
#     record = medaldict[data]
#     topMedals += str(data) + ": " + str(record) + "\n"


# @app.route('/')
# def home():
#     if 'token' in session:
#         bearer_client = APIClient(session.get('token'), bearer=True)
#         current_user = bearer_client.users.get_current_user()
#         response = requests.get(f'https://statcore01.pcon.statrepo.com/api/players/{current_user.username}')
#         resp_json=response.json()
#
#         kills = resp_json["Summary"]["Kills"]
#         deaths = resp_json["Summary"]["Deaths"]
#         wins = resp_json["Summary"]["Won"]
#         lost = resp_json["Summary"]["Lost"]
#
#         return render_template("index.html", current_user=current_user, level=a)
#     return render_template('index.html', oauth_uri=OAUTH_URL)


#cd C:\Users\Travi\OneDrive\Desktop\flasksite






if __name__ == "__main__":
    partial_run = partial(app.run, host="192.168.1.118", port=4444, debug=True, use_reloader=False)
    # app.run(host = '192.168.1.118', port = 4444)
    # app.run(debug=True)
    t = Thread(target=partial_run)
    t.start()
    bot.run("")
