from functions import download_image
prefix = $$
if message.content.startswith(f'{prefix}download_image'):
    url = message.content.split()[1] except Exception else await message.channel.send(f'`Usage: {prefix}download_image <URL>`')
    await message.channel.send('Here's Your Image!', file=discord.File(download_image(url)))
    
