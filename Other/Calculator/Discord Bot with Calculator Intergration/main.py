import discord #Imports required modules
import base64
import parsingengine

token = ("YOUR-TOKEN-HERE") # Connects to your bot
ans = 0
seperator = ' '
## Bot setup

client = discord.Client() # Creates the bot client

@client.event
async def on_ready(): # When bot is ready, prints out bot name.
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message): # When a message is sent in the discord server,
        if message.content.startswith('/calc'): # If it begins with /calc
            calculation = message.content
            calculation = calculation.split(' ')
            calculation = calculation[1:len(calculation)] # Finds all of the message that isnt /calc
            calculation = seperator.join(calculation)
            ans = parsingengine.parsingengine(calculation) # Calculates it
            await message.channel.send(ans) # Outputs answer


client.run(token) # Runs bot