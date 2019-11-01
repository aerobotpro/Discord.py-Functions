import discord #Discord py

# SECRET TOKEN
token = "NDFDSasdf54Wga#WFh.iDSaAgtyessdfgkjdflgl.rfdg"

client=discord.Client() #DEFINES CLIENT OBJECT

prefix = "$$" # Here's your prefix!


# ASYNCHRONOUS DEFINITIONS/SEQUENCE BEGINS

# ON_READY():    
@client.event # "Called when the client is done preparing the data received from Discord."
async def on_ready():# "Usually after login is successful and the Client.guilds and co. are filled up."
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))

    #SETTING RICH PRESENCE
    activity = discord.Activity(name="my first bot come to life!", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
   
#ON_MESSAGE():    
@client.event # "Called when a Message is created and sent."
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix("hello")):
        # Do Jobs Here // ...
        reply = str(f"{message.content.replace(prefix, "")}!")
        await message.channel.send(reply)

    if message.content.startswith(prefix("goodbye")):
        # Do Jobs Here // ...
        reply = str(f"{message.content.replace(prefix, "")}!")
        await message.channel.send(reply)


def prefix(string):
    return f"{prefix}{string}"


client.run(token)   #INITIALIZE CLIENT/CONNECTION 
