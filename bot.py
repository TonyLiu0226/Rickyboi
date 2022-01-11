#IMPORTANT: LINES 124-179 IS THE ROCK PAPER SCISSORS COMMAND THAT WAS ADDED TO THE EXISTING BOT DURING LHD BUILD.
import json
from re import X
from requests.sessions import extract_cookies_to_jar
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord import FFmpegPCMAudio
import random
import asyncio
import youtube_dl
import os
import requests
import datetime
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
import sys
from collections import Counter
import calendar
from bs4 import BeautifulSoup
import traceback
from discord.ui import Button, View
key = "your_key" 

member_list = {}
WEATHER_URL = "http://api.openweathermap.org/data/2.5/weather?"
FORECAST_URL = "http://api.openweathermap.org/data/2.5/forecast?"
TRANSLINK_API = "your_api"
TOKEN_ID = "use_your_own_bot_token" 

intents = discord.Intents().all()
bot = commands.Bot(command_prefix="?", intents=intents)
now = datetime.now()
NUM_TROLLSONGS = 7
NUM_PLAYSONGS = 2
NUM_ITERATIONS = 25

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]



@bot.command(aliases = ['c'], help="The classic cheesetouch game you used to play as a kid, but discord edition")
async def cheesetouch(ctx):
    try:
        members = []

        for member in ctx.guild.members:
            if not member.bot:

                if not member.name in member_list:
                    member_list[member.name] = 0
                
                members.append(member)

        print(member_list) #a list of all server members
        #BOT OWNER IS IMMUNE FROM CT, REPLACE 'OWNER' WITH YOUR DISCORD USERNAME
        member_list['OWNER'] = 2

        if member_list.get(ctx.author.name) != 0: #if the user calling the command currently has the cheesetouch, then they pass it on to another user
            #removes ct from previous ct holder
            for key in member_list.keys():
                if member_list.get(key) == 1:
                    member_list[key] = 0

            i = random.randint(1, len(members))
            await ctx.send("{}".format(members[i-1].mention) + " Has the cheesetouch")
            member_list[members[i-1].name] = 1
            member_list["OWNER"] = 2 #remember bot owner is always immune


        else: #if the user calling the command does not have the cheesetouch atm, then they can see who currently has it, but they can't pass it on to anyone else
            #iterate through member list and find the dude that has a 1.
            for key in member_list.keys():
                if member_list.get(key) == 1:
                    await ctx.send(key + " currently has the cheesetouch")

        print(member_list)

    except Exception as e:
        print(e)



@bot.command(aliases = ['l'], help="A simple guessing game. You win the 'lottery' if you get the number right. (This is harder than it seems, you'll see kekw)")
async def lottery(ctx):
    try:
        i = 6
        ans = random.randint(1,100)
        print(ans)
        await ctx.send("{}".format(ctx.author.mention) + " Please enter a number from 1 to 100") #allows user to input a guess

        def check(message):
                return message.channel == ctx.message.channel and message.author == ctx.message.author

        while (i > 0):

            input = await bot.wait_for("message", timeout=30, check=check) #user has 30 seconds to input a guess before game quits
            print(input.content)

            if (input.content == str(ans)): #correct guess
                await ctx.send("{}".format(ctx.author.mention) + " congrats, you won the lottery")
                await ctx.send("https://preview.redd.it/zsquuygt2zd41.jpg?auto=webp&s=d9228c1fcdad49a8cb142927ab576fd66bbc7c7f") #lottery meme
                return

            else: #wrong guess
                i = i-1
                if i > 0:
                    await ctx.send("{}".format(ctx.author.mention) + " Your guess was not correct, please try again, " +str(i) + " attemps remaining")
        
        #if out of attempts
        await ctx.send("HAHAHAHA {}".format(ctx.author.mention) + " lost! The correct answer was " + str(ans))
        await ctx.send("https://yt3.ggpht.com/ytc/AKedOLRc_LJeSrh2Mo5PUSgGRnVmQ776qAhrzTzGsVho=s900-c-k-c0x00ffffff-no-rj")     #kekw face

    except Exception as e:
        print(e)
        await ctx.send ("Failed, here's the reason why: " +e)

#################################################################################################################################################################
#       This command (below) was completed during day 2 of LHD: Build. All other commands were previously there before the hackathon, and not part of the challenge.
#################################################################################################################################################################

@bot.command(aliases=['rps'], help="Straightforward, just rock paper scissors. Keeps track of user wins")
async def rockPaperScissors(ctx):
    try:
        
        button1 = Button(emoji="⛰️", style=discord.ButtonStyle.grey)
        button2 = Button(emoji="📰", style=discord.ButtonStyle.grey)
        button3 = Button(emoji="✂️", style=discord.ButtonStyle.grey)

        #rock is 1, paper is 2, and scissors is 3. Dependencies: 2 > 1, 3 > 2, 1 > 3
        async def onClickListener1(interaction):
            
            player = 1
            AI = random.randint(1, 3)
                
            if (AI == 2):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Lost :cry:, I picked paper", view=None)
            elif (AI == 3):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Won :smile:, I picked scissors", view=None)
            else:
                await interaction.response.edit_message(content=f"{ctx.author.mention} The game is a tie cuz I also picked rock lol", view=None)

        async def onClickListener2(interaction):
            player = 2
            AI = random.randint(1, 3)

            if (AI == 3):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Lost :cry:, I picked scissors", view=None)
            elif (AI == 1):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Won :smile:, I picked rock", view=None)
            else:
                await interaction.response.edit_message(content=f"{ctx.author.mention} The game is a tie cuz I also picked paper lol", view=None)
        
        async def onClickListener3(interaction):
            player = 3
            AI = random.randint(1, 3)

            if (AI == 1):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Lost :cry:, I picked rock", view=None)
            elif (AI == 2):
                await interaction.response.edit_message(content=f"{ctx.author.mention} You Won :smile:, I picked paper", view=None)
            else:
                await interaction.response.edit_message(content=f"{ctx.author.mention} The game is a tie cuz I also picked scissors lol", view=None)
        
        button1.callback = onClickListener1
        button2.callback = onClickListener2
        button3.callback = onClickListener3

        view = View(timeout=15)
        view.add_item(button1)
        view.add_item(button2)
        view.add_item(button3)
        await ctx.send("Choose rock, paper or scissors", view=view)

    except Exception as e:
        traceback.print_exc()
        
        
        
@bot.command (aliases = ['n'])    
async def announce(ctx):
    await ctx.send("Please enter a message for me to announce")

    def check(message):
        return message.channel == ctx.message.channel and message.author == ctx.message.author
    
    input = await bot.wait_for("message", timeout=30, check=check) #user has 30 seconds to enter a message to announce
    print(input.content)

    try:
        for i in range (NUM_ITERATIONS): #will repeatedly ping everyone NUM_ITERATIONS amount of times.
            await ctx.send(f"<@everyone>") 
            await ctx.send("{}".format(input.content)) 
    except Exception as e:
        print(e)



@bot.command(aliases = ['a'])
async def add(ctx, *numbers):
    try:
        sum = 0
        print(numbers)
        k = []
        for n in range (len(numbers) - 1): #adds sum while formatting the equation that is printed at the end
            k.append(numbers[n])
            sum += int(numbers[n])
            k.append(" + ")
        
        k.append(numbers[len(numbers) - 1])
        sum += int(numbers[len(numbers) - 1])
        k.append(" equals:")
    
        print(sum)
        embed=discord.Embed(title= " ".join(k), description= str(sum), color=0xFF5733) #prints out the equation as the title, then the sum as the description
        await ctx.send(embed=embed)

    except Exception as e:
        print(e)
        await ctx.send("{}".format(ctx.author.mention) + "OOPS, invalid number or you entered too many numbers for an embed to display kekw")



@bot.command(name = 'average', help='calculates the weighted average of user inputted numbers and weights. Useful for GPA calculations.', aliases = ['avg'])
async def average(ctx, *args):
    try: 
        value = []
        weight = []
        sum = 0
        weightsum = 0
        for x in args:
            it = x.split(",")

            #if weight is not specified (args do not have ,) then simply put the weight as 1
            if len(it) == 1:
                value.append(it[0])
                weight.append(1)

            elif len(it) == 2:
                value.append(it[0])
                if int(it[1]) < 0:
                    await ctx.send("{}".format(ctx.author.mention) + "Bruh why would you enter weights that are less than 0")
                    #Design choice: weights cannot be less than zero, to make calculations simpler
                    raise Exception("Bruh why would you enter weights that are less than 0")  
                weight.append(it[1])
                
                #wrong format
            else:
                await ctx.send("{}".format(ctx.author.mention) + "Invalid input, please enter your values and weights in one of the following format: value1,weight1 value2,weight2 etc... OR value1 value2 etc... Ensure they are all valid numbers")
                value.append(0.0)
                weight.append(0.0)
                break

        #calculates the average
        print(value)
        print(weight)
        for i in range (len(value)):
            a = float(value[i])
            b = float(weight[i])
            sum += float(a * b)
            weightsum += b

        average = float(sum/weightsum)
        embed=discord.Embed(title="Your weighted average is:", description= str(average), color=0xFF5733)
        if average < 50: #F
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT9D6zneddyBjmc3M4dro8aPywrlM-SHJuP7Q&usqp=CAU")
        elif average < 55: #D
            embed.set_thumbnail(url="https://cdn.gottman.com/wp-content/uploads/2014/02/D-is-for-Defensiveness_HI.jpg")
        elif average < 68: #C
            embed.set_thumbnail(url="https://us.123rf.com/450wm/logomimi/logomimi2102/logomimi210200810/163861624-grade-result-c-red-exam-score-vector-illustration.jpg?ver=6")
        elif average < 80: #B
            embed.set_thumbnail(url="https://www.photos-public-domain.com/wp-content/uploads/2012/07/b-school-letter-grade.jpg")
        else: #A
            embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTuDkIv-DepFa3h8FjHQ2WDwCSNuhu1qwCB7A&usqp=CAU")
        await ctx.send(embed=embed)
        
    except Exception as e:
        await ctx.send("{}".format(ctx.author.mention) + " lol you didn't enter valid numbers or you had a total weight of 0 and thus got an error due to dividing by 0!")
        print(e)



@bot.command(aliases = ['rickroll', 'p'], help='Plays music, but for now it is only 2 songs kekw', pass_context = True)
async def play(ctx):
    try: 
        if ctx.author.voice:
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            i = random.randint(1,NUM_PLAYSONGS)
            if i == 2:
                source = FFmpegPCMAudio('rr.wav') #rickroll
            if i == 1:
                source = FFmpegPCMAudio('st1.mp3') #weird noises that arent rickroll
            
            voice.play(source)

            if i == 2:
                await ctx.send("Hahaha, you got rickrolled pog")
            else:
                await ctx.send("Enjoy these weird ass noises")
    
        else:
            await ctx.send("WTF are you doing man, you gotta be in a voice channel for me to play music!") #if user calls the command when not in voice channel
    
    except Exception as e:
        print(e)
        await ctx.send("Failed, reason: " + e)



@bot.command(aliases = ['r'], help= 'Plays loud music, watch your ears!', pass_context = True)
async def earrape(ctx):
    try: 
        if ctx.author.voice:
            
            channel = ctx.message.author.voice.channel
            voice = await channel.connect()
            i = random.randint(1, NUM_TROLLSONGS)
            print(i)

            #7 of the most meme songs on there for now...
            if i == 1:
                source = FFmpegPCMAudio('WII.mp3') 
            if i == 2:
                source = FFmpegPCMAudio('SWED.mp3')
            if i == 3:
                source = FFmpegPCMAudio('TTT.mp3')
            if i == 4:
                source = FFmpegPCMAudio('TS.mp3')
            if i == 5:
                source = FFmpegPCMAudio('LYDS.mp3')
            if i == 6:
                source = FFmpegPCMAudio('TIKC.mp3')
            if i == 7:
                source = FFmpegPCMAudio('DDS.mp3')

            voice.play(source)
    
        else:
            await ctx.send("WTF are you doing man, you can't get earraped if ur not in a voice channel") #if user calls command when not in voice channel
    
    except Exception as e:
        print(e)
        await ctx.send("Failed, reason: " + e)



@bot.command(name = 'exit', help = 'disconnects bot from channel', aliases = ['e'])
async def exit(ctx):
    if ctx.author.voice:
        await ctx.voice_client.disconnect()
    
    else:
        await ctx.send("HAHAHAHA You aren't in a voice channel, can't kick me out xP :)") #if user tries to kick the bot out of voice when not in a voice channel



@bot.command(help = 'searches urban dictionary for a definition of the given term', aliases = ['ud', 'define', 'definition'])
async def urban(ctx, *args):
    try:
        urlend = ("%20".join(args[:]))
        url = "https://www.urbandictionary.com/define.php?term="+urlend
        print(url)
        text1 = requests.get(url, timeout=5) 

        #web scrapes the given URL using bs4 to find the definition. Finds the first definition that is on the page and prints it.
        s = BeautifulSoup(text1.text, 'lxml')

        t = s.find_all('div', class_='meaning')

        embed=discord.Embed(title="The official urban dictionary definition of " +(" ".join(args[:])) +":", description= t[0].text, color=0xFF5733)
        embed.set_thumbnail(url="http://www.userlogos.org/files/logos/Str1ke/UrbanDict.png") #urban dictionary logo
        await ctx.send(embed=embed)

    except Exception as e:
        await ctx.send("{}".format(ctx.author.mention) + "Oops, I can't find any definitions")
        print(e)
    


@bot.command(name = 'bus', help = 'gives the user the time of the next bus departure from a bus stop', aliases = ['nb'])
async def nextBus(ctx,stop_num):
    try:
        headers = {"accept":"application/JSON"}
        url = "https://api.translink.ca/rttiapi/v1/stops/" + stop_num + "/estimates?apikey=" + TRANSLINK_API + "&count=1&timeframe=1440"
        
        r = requests.get(url,headers=headers)
        bus_data = r.json()[0]

        #accesses bus route, destination, and departure time from the json data
        schedule = bus_data['Schedules'][0]
        await ctx.send("Bus route: " + bus_data['RouteNo'] + " " + bus_data['RouteName'] + " to " + schedule['Destination'])
        busTime = (schedule['ExpectedLeaveTime'])
        
        #Formats the time to the correct format to calculate the time difference between now and the departure time
        datetime_busTime = datetime.strptime(busTime, '%I:%M%p')
        hour = datetime_busTime.hour
        min = datetime_busTime.minute

        busTime = datetime(now.year, now.month, now.day, hour, min)

        #prints out time until departure time
        timeToNextBus = busTime - now
        timeInMin = int((timeToNextBus.total_seconds())/60)
        await ctx.send("Arriving in: " +str(timeInMin) + " minutes")
        if timeInMin >= 20: 
            await ctx.send("Enjoy waiting :rofl:")


    except Exception as e:
        await ctx.send("This bus stop number does not exist. Please enter a valid 5-digit bus stop")
        print(e)



@bot.command(help="Gets the weather forecast for the specified city" )
async def weather(ctx, *city):
    try:
        c = " ".join(city)
        URL = WEATHER_URL + "q=" + c + "&appid=" + key
        response = requests.get(URL)
        data = response.json()
        print(URL)

        m = data['main']
        k = data['weather']
        print(k)
        if len(k[0]) == 1:
            raise Exception("No city found!") #if the main or weather data list, it means there is no data available for the city entered, likely because the city doesn't exist

        print(m)
        
        #note temperatures in the json data is in kelvin, we convert to celcius because who uses kelvin other than chemists
        e = discord.Embed(title="The weather for " +c + " is",
                description= ("The current temperature is: " +str(int(m.get('temp') - 273.15)) + " C" + "\n" +
                "It is currently " +str(k[0].get('description')) + " outside" + "\n" +
                "The daily high is: " +str(int(m.get('temp_max') - 273.15)) + " C" + "\n" +
                "The daily low is: " +str(int(m.get('temp_min') - 273.15)) + " C"))
        e.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcShaziZ8JDaMtWQyj_DCjKxnKp4f4X8tfeOig&usqp=CAU") #weather logo
        await ctx.send(embed = e)

    except Exception as f:
        print(f)
        await ctx.send("{}".format(ctx.author.mention) +" NO CITY FOUND!")



@bot.command(help="Gets the 5 day forecast for a specified city", aliases = ['forecast'])
async def weatherForecast(ctx, *city):
    try:
        c = " ".join(city)
        URL = FORECAST_URL + "q=" + c + "&appid=" + key
        response = requests.get(URL)
        data = response.json()
    
        l = data['list']

        weatherArr = [int((l[0]['main']['temp'])-273.15), int((l[7]['main']['temp'])-273.15), int((l[15]['main']['temp'])-273.15), 
        int((l[23]['main']['temp'])-273.15), int((l[31]['main']['temp'])-273.15), int((l[39]['main']['temp'])-273.15)]

        conditionArr = [l[0].get('weather')[0].get('description'), l[7].get('weather')[0].get('description'), l[15].get('weather')[0].get('description'), 
        l[23].get('weather')[0].get('description'), l[31].get('weather')[0].get('description'), l[39].get('weather')[0].get('description')]
        day = ["Today (3h from now)", "Tomorrow", "In 2 days", "In 3 days", "In 4 days", "In 5 days"]

        e = discord.Embed(title= f"{c} Weather", color=0xFF5733)

        e.add_field(name=f'**{day[0]}**', value=f'> Weather: {conditionArr[0]}\n> Temperature {weatherArr[0]} C',inline=False)
        e.add_field(name=f'**{day[1]}**', value=f'> Weather: {conditionArr[1]}\n> Temperature {weatherArr[1]} C',inline=False)
        e.add_field(name=f'**{day[2]}**', value=f'> Weather: {conditionArr[2]}\n> Temperature {weatherArr[2]} C',inline=False)
        e.add_field(name=f'**{day[3]}**', value=f'> Weather: {conditionArr[3]}\n> Temperature {weatherArr[3]} C',inline=False)
        e.add_field(name=f'**{day[4]}**', value=f'> Weather: {conditionArr[4]}\n> Temperature {weatherArr[4]} C',inline=False)
        e.add_field(name=f'**{day[5]}**', value=f'> Weather: {conditionArr[5]}\n> Temperature {weatherArr[5]} C',inline=False)

        await ctx.send(embed=e)

    except Exception as e:
        print(e)
        traceback.print_exc()
        await ctx.send(f"{ctx.author.mention} You have entered an invalid city!")
        


@bot.command(help="generates a calendar in the form of an HTML file with the user specified year and month. Format yyyy mm", aliases = ['calendar'])
async def generateCalendar(ctx, year, month):
    
    try:
        if (int(month) < 1 or int(month) > 12):
            await ctx.send("Invalid month entered, please enter a number between 1 and 12 for month, with 1 being January, 2 being February, etc")
            raise Exception("Invalid month entered, please enter a number between 1 and 12 for month, with 1 being January, 2 being February, etc")
        elif (int(year) < 1 or int(year) > 5000):
            await ctx.send("Invalid year entered, please enter a year between 1 and 5000")
            raise Exception("Invalid year entered, please enter a year between 1 and 5000")
        else:
            
            m = int(month)
            y = int(year)
            cal = calendar.HTMLCalendar(calendar.SUNDAY)
            state = cal.formatmonth(y, m, 0)
            with open('calendar.html', 'w') as f:
                f.write(state) 

            await ctx.send("{}".format(ctx.author.mention) + "Here is ur calendar m8")    
            await ctx.send(file=discord.File('calendar.html')) #user must download file and open in a web browser to see the calendar in text form

    except Exception as e:
        await ctx.send("{}".format(ctx.author.mention) + "Bruh, you didn't enter a valid month or year, please try again")
        print(e)



@bot.command(help="Find what day it will be a specified number of days from now. Enter a negative number to find what day it was that number of days ago", aliases = ['DFN', 'days'])
async def daysFromNow(ctx, num):
    try:
        n = int(num)
        td = timedelta(days = n)
        result = datetime.now() + td
        r = datetime.strftime(result, '%B %d, %Y')
        wd = week[result.weekday()]
        print(r)
        if n >= 0:
            embed=discord.Embed(title= num + " days from now is: ", description= (wd + ", " + r), color=0xFF5733)
            await ctx.send(embed = embed)
        else:
            embed=discord.Embed(title= str(abs(n)) + " days ago was: ", description= (wd + ", " + r), color=0xFF5733)
            await ctx.send(embed = embed)

    except Exception as e:
        print(e)
        await ctx.send("{}".format(ctx.author.mention) + "You entered an invalid number of days!")



@bot.command(help="Find days until a specified date. Date format is: yyyy m d", aliases = ['ND', 'until'])
async def daysUntil(ctx, year, month, day):
    try:
        if (int(month) < 1 or int(month) > 12):
            await ctx.send("Invalid month entered, please enter a number between 1 and 12 for month, with 1 being January, 2 being February, etc")
            raise Exception("Invalid month entered, please enter a number between 1 and 12 for month, with 1 being January, 2 being February, etc")
        elif (int(year) < 1 or int(year) > 5000):
            await ctx.send("Invalid year entered, please enter a year between 1 and 5000")
            raise Exception("Invalid year entered, please enter a year between 1 and 5000")
        else:
            m = int(month)
            y = int(year)
            if m == 2: #finds out whether february will have 28 or 29 days
                if y % 4 == 0 and y % 100 != 0:
                    if (int(day) < 1 or int(day) > 29):
                        raise Exception("Invalid date entered")
                elif y % 100 == 0 and y % 400 == 0:
                    if (int(day) < 1 or int(day) > 29):
                        raise Exception("Invalid date entered")
                else:
                    if (int(day) < 1 or int(day) > 28):
                        raise Exception("Invalid date entered")
            
            elif (m == 4 or m == 6 or m == 9 or m == 11): #these months have 30 days
                if (int(day) < 1 or int(day) > 30):
                    raise Exception("Invalid date entered")

            else:
                if (int(day) < 1 or int(day) > 31): #these months have 31 days
                    raise Exception("Invalid date entered")

            d = int(day)
            date1 = datetime(y, m, d, 0, 0, 0, 0) #time difference will always be calculated to 0:00am of the specified day, to avoid ambiguities
            td = date1 - datetime.now()
            days = td.total_seconds()/86400
            if days < 0 and days > -1: #if called at 23:59, then it is still the same date, but time difference from 0:00 is almost -1 days difference. We still consider it same day though.
                d = 0
                embed=discord.Embed(title= year + "/" + month + "/" + day + " is today!", color=0xEE5733)
                await ctx.send(embed = embed)
            elif days > 0:  #if greater than 0, add 1 to the days, to account for truncating between float and int (while still being sure that no matter what time you call the command, tomorrow is always 1 day away from today)
                d = int(days) + 1
                embed=discord.Embed(title= "Number of days until " +year + "/" + month + "/" + day + " is:",
                description= (str(d)), color=0xEE5733)
                await ctx.send(embed = embed)
            else:
                d = int(days) #it doesn't matter actually, we won't return a number of days, just tell user that it has already passed and there is no use finding the time until a date that already passed
                embed=discord.Embed(title= year + "/" + month + "/" + day + " has already passed!",
                description= ("Next time, maybe enter a date that hasn't already passed"), color=0xEE5733)
                await ctx.send(embed = embed)
  
    except Exception as e:
        await ctx.send("{}".format(ctx.author.mention) + "Bruh you didn't enter a valid date m8")
        print(e)



@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send("ERROR: NO COMMAND WITH THAT NAME WAS FOUND!")



bot.run(TOKEN_ID)
