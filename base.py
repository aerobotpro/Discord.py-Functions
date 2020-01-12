import discord #Discord py

# SECRET TOKEN
token = "NDFDSasdf54Wga#WFh.iDSaAgtyessdfgkjdflgl.rfdg"

client=discord.Client() #DEFINES CLIENT OBJECT

prefix = "$$" # Here's your prefix!

rp = "my first bot come to life!"

# ASYNCHRONOUS DEFINITIONS/SEQUENCE BEGINS

# ON_READY():

@client.event
#(on_ready)
# "Called when the client is done preparing the data received from Discord."
# "Usually after login is successful and the Client cache is ready."
async def on_ready():
    print('-\n[Ok] - Succesfully logged in as {0.user} Via Discord Official API!'.format(client))

    #SETTING RICH PRESENCE ON READY
    activity = discord.Activity(name=rp, type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
   
#ON_MESSAGE():
# "Called when a Message is recieved."
@client.event 
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(f"{prefix}hello"):
        # Do Jobs Here // .
        await message.channel.send(f"Hello <@{message.author.id}>!")
        
    if message.content.startswith(f"{prefix}add"):
        # Adding 2 numbers like: {prefix}add 1 1
        #Output: >>> "1 + 1 = 2, author.mention!"
        int_1 = int(message.content.split()[1])
        int_2 = int(message.content.split()[3])
        answer = int(int_1 + int_2)
        await message.channel.send(f"{str(int_1)} + {str(int_2)} = {str(answer)}, <@{message.author.id}>!")

client.run(token)   #INITIALIZE CLIENT/CONNECTION 
