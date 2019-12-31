#Cold-Pasted, you'll need to fix/implement this to your code for it to work properly until I can get to this.
#from download_image_from_url import download_image
if message.content.startswith(f'{prefix}salt_shade'):
    
    
    p = message.content.replace(#Split our args and remove the junk ;)
        f'{message.content.split()[0]} ',"")
    #Gracefully stripping away delims + first arg leaves us with a user-id from a mention :)
    .replace(" ", "")
    .replace("<", "")
    .replace("@", "")
    .replace(">", "")
    .replace("!", "")
    
        #"Extra" Safe Error-Handling
        exp = False 
        
        # Check if not base of ten (or None) if so then throw fail.
        # Also fail if more than 1 arg or no args.
        try:
            p = int(p)
        except Exception: 
            exp = True
            pass
        
        if exp == False: # If all is well:
            member = discord.utils.get(message.guild.members, id=p)
            
            #Check to see if valid member was mentioned & retrieved valid object
            if member is not None: 
                cont = True
                try:
                    fname = utils.download_image(str(member.avatar_url))
                except Exception as eee:
                    cont = False
                    print(str(eee))
                    await message.channel.send("Couldn't Get An Avatar For This Member!\n> Valid User?\n> Is GIF?")

                #Begin PIL job    
                try:
                    #Show typing while in coro job.
                    async with message.channel.typing():
                        img = Image.open(fname) # Open img
                        km = (-2, -1,  0, -1,  1,  1, 0,  1,  2) # Throw Salt-Shade params to the stack.
                        k = ImageFilter.Kernel(size=(3, 3), kernel=km,# Process Image
                            scale=sum(km),  # default
                            offset=0  # default
                            )
                        img.filter(k).save(fname)
                        #save image, my DOWNLOAD_IMG function
                        #returns the filepath as "fname"
                except Exception as e:
                    #log(str(e)) If you need to debug PIL issues. # Issue 127
                    cont = False
                    
                if cont == True: # If all is good, return image to Discord!
                    await message.channel.send(
                        f"**Here's Your Image <@{message.author.id}>!**",
                        file=discord.File(fname))
                    remove(fname)
                    # Remove the file as its no longer needed.
                    
                #Failed To Download image, wide range of possible errors, use debugging ABOVE ^^ (#Issue 127)
                else:
                    remove(fname)
                    # Remove the file as its no longer needed.
                    await message.channel.send(
                        "**```diff\n-Error!\nCould Not Process Image! GIF mabye?\n```**"
                        )
                    
            else: #MEMBER is None
                await message.channel.send(
                    "Couldn't Find This Member!"
                    )
