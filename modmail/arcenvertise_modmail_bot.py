import discord #Discord py

# SECRET TOKEN
token = "NDFDSasdf54Wga#WFh.iDSaAgtyessdfgkjdflgl.rfdg"

client=discord.Client() #DEFINES CLIENT OBJECT

prefix = "$$" # Here's your prefix!


# ASYNCHRONOUS DEFINITIONS/SEQUENCE BEGINS


@client.event
async def on_ready():
    log.log('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))

    #SETTING RICH PRESENCE
    activity = discord.Activity(name="stuff", type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
   
    
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(prefix()):
        reply = str(f"{message.content.replace(prefix, "")}!")
        await message.channel.send(reply)



def prefix(string):
    return f"{prefix}{string}"
    
def make ticket(message):
    #//stuff

client.run(token)
