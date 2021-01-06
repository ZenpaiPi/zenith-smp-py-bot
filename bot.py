import discord
import requests
import json
import datetime

client = discord.Client()

TOKEN = 'Nzk2MTgxMjk3NzE3ODM3ODM0.X_ULnQ.p3Vqfmax9WSKccnU9u7tDTSNUiQ'

@client.event
async def on_ready():
    print(f'{client.user} Has Connected To The Discord API')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='To ZenithSMP'))

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Welcome To ZenithSMP!'
)       

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content == 'zenith.time':
        r = requests.get('http://api.weatherstack.com/current?access_key=94a407caabef3ae8eea168ed85fd3a55&query=Shah%20Alam')
        weather = json.loads(r.text)
        currentweather = (weather["current"])
        forecast = (currentweather["weather_descriptions"])
        temperature = (currentweather["temperature"])
        icon = (currentweather["weather_icons"])
        stricon = ' '.join(map(str, icon))
        strfore = ' '.join(map(str, forecast))
        now = datetime.datetime.now()
        timeString = now.strftime("%Y-%m-%d %H:%M")
        fullsentence = 'It Is Now {} Where Zenith Lives, The Forecast There Is {} ,And The Temperature There Is {} Degrees Celcius.'.format(timeString, strfore, temperature)
        await message.channel.send(fullsentence)

    if message.content == 'zenith.pingcoco':
        await message.channel.send()

	if message.content == 'zenith.ping':
        await message.channel.send()
	
	if message.content == '':
        await message.channel.send()
		
	if message.content == '':
        await message.channel.send()
		
	if message.content == '':
        await message.channel.send()

	if message.content == '':
        await message.channel.send()

	if message.content == '':
        await message.channel.send()

	if message.content == '':
        await message.channel.send()

	if message.content == '':
        await message.channel.send()	

client.run(TOKEN)


