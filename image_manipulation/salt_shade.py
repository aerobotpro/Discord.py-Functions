#Cold-Pasted, you'll need to fix/implement this to your code for it to work properly until I can get to this.
#from download_image_from_url import download_image
prefix = '$'

if message.content.startswith(f'{prefix}salt_shade'):
        pyyp1 = message.content.replace("at.cartoonify","").replace(" ", "").replace("<", "").replace("@", "").replace(">", "").replace("!", "")
        exp = False
        try:
            pyyp1 = int(pyyp1)
        except Exception:
            exp = True
            pass
        if exp == False:
            member = discord.utils.get(message.guild.members, id=pyyp1)
            if member is not None:
                cont = True
                try:
                    fname = utils.download_image(str(member.avatar_url))
                except Exception as eee:
                    cont = False
                    print(str(eee))
                    await message.channel.send(bold("Couldn't Get An Avatar For This Member!\n> Valid User?\n> Is GIF?"))
                try:
                    async with message.channel.typing():
                        img = Image.open(fname)
                        km = (-2, -1,  0, -1,  1,  1, 0,  1,  2)
                        k = ImageFilter.Kernel(size=(3, 3), kernel=km,
                            scale=sum(km),  # default
                            offset=0  # default
                            )
                        img.filter(k).save(fname)
                except Exception as eeds:
                    log.log(str(eeds))
                    cont = False
                if cont == True:
                    await message.channel.send(f"**Here's Your Image <@{message.author.id}>!**", file=discord.File(fname))
                    remove(fname)
                else:
                    remove(fname)
                    await message.channel.send("**```diff\n-Error!\nCould Not Process Image! GIF mabye?\n```**")
            else:
                await message.channel.send(bold("Couldn't Find This Member!"))
