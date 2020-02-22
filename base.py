import discord #Discord py
from datetime import datetime


# SECRET TOKEN
token = "NjQ5MDAzNTkwMjU3NzM3NzM5.XhqjOw.c0vqUU3I_ZWNXw-huHoNRc3BA_8"

client=discord.Client() #DEFINES CLIENT OBJECT

prefix = "$$" # Here's your prefix!

rp = "my first bot come to life!"

class glbl:
    begin = datetime.now()
    
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
    if message.author == client.bot:
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

    if message.content.startswith(f"{prefix}uptime"):
        await message.channel.send(f"I have been up for {str(uptime())} minutes!")
        
def uptime():
    #Get timestamp when called.
    now = datetime.now()
    if glbl.begin > now:
        uptime = glbl.begin - now
    else:
        uptime = now - glbl.begin
    return int(round(uptime.total_seconds() / 60))

client.run(token)   #INITIALIZE CLIENT/CONNECTION 
