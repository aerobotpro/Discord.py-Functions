 # Cleanup all messages by member in text_channels on member remove/leave guild event.     
search_depth = 500
@client.event
async def on_member_remove(member):
    count = 0
    failed = False
    stuff = str()
    try:  
        guild = client.get_guild(member.guild.id)
        for channel in guild.text_channels:
            async for message in channel.history(limit=search_depth):
                if message.author.id == member.id:
                    await message.delete()
                    count += 1
    except Exception as EE:
        failed = True
        stuff = f"**logging:**\n```\ndiff\n-{str(EE)}```"
    channel = client.get_channel(settings.logging_channel)   #Any Channel ID Can Go Here, As Long As In Guild!** 
    if failed == False:
        stuff = f"**Logging: <@{member.id}> just left the guild. Successfully Cleared `{count}` messages!**"
    await channel.send(stuff)
