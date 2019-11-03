from functions import download_image
prefix = $$

if message.content.startswith(f'{prefix}download_image'):
    continue_ = True
    
    url = message.content.split()[1] except Exception:
        await message.channel.send(f'`Usage: {prefix}download_image <URL>`')
        continue_ = False
        
    if continue_ == True: await message.channel.send('Here's Your Image!', file=discord.File(download_image(url)))
    
