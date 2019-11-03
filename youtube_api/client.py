#Snippet from my "YouTube Assistant" bot, enjoy!
from functions import *

class amount:
    #Video/Channel/Playlist - max results amounts :)
    video = 10
    channel = 4
    playlist = 2

prefix = $$    

if message.content.startswith(f"^youtube") or message.content.startswith(f"^Youtube") or message.content.startswith(f"^YouTube"):
    query = str(message.content.replace(f"{message.content.split()[0]} ", ""))
    parser = argparse.ArgumentParser()
    parser.add_argument('--q', help='Search term', default=query)
    parser.add_argument('--max-results', help='Max results', default=25)
    args = parser.parse_args()
    try:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=DEVELOPER_KEY)

      # Call the search.list method to retrieve results matching the specified
      # query term.
        search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_res).execute()

        videos = []
        channels = []
        playlists = []

        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                videos.append('%s (%s)' % (search_result['snippet']['title'],
                                           search_result['id']['videoId']))
            elif search_result['id']['kind'] == 'youtube#channel':
                channels.append('%s (%s)' % (search_result['snippet']['title'],
                                             search_result['id']['channelId']))
            elif search_result['id']['kind'] == 'youtube#playlist':
                playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                              search_result['id']['playlistId']))





        embed = discord.Embed(title=f"__Search Results__", description=" ", url='https://thebothub.host', color=0xFF0000)
        embed.set_author(name="YouTube Assistant", url='https://aero-bot.pro/', icon_url='https://cdn.discordapp.com/attachments/635586855567622147/636112733439262742/maxresdefault.jpg')
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/635586855567622147/636121471659540480/giphy.gif")

        for x in range(0, len(videos)):
            special_link = videos[x].split()[len(videos[x].split()) - 1]
            title = convert_html(videos[x].replace(f" {special_link}", ""))
            special_link = special_link.replace("(", "").replace(")", "")
            link = str("https://www.youtube.com/watch?v=" + special_link)

            embed.add_field(name=f" __Video:__\n#{str(int(x + 1))} | {title}", value=f"[Watch Video]({link})", inline=True)

            if x == amount.video: break 


        for x in range(0, len(channels)):
            special_link = channels[x].split()[len(channels[x].split()) - 1]
            user = convert_html(channels[x].replace(f" {special_link}", ""))
            special_link = special_link.replace("(", "").replace(")", "")
            link = str(f"https://www.youtube.com/channel/{special_link}")

            embed.add_field(name=f"__Channel:__\n#{str(int(x + 1))} | {user}", value=f"[Go To Channel]({link})", inline=True)

            if x == amount.channel: break 



        for x in range(0, len(playlists)):
            special_link = playlists[x].split()[len(playlists[x].split()) - 1]
            playlist = convert_html(playlists[x].replace(f" {special_link}", ""))
            special_link = special_link.replace("(", "").replace(")", "")
            link = str(f"https://www.youtube.com/playlist?list={special_link}")

            embed.add_field(name=f"__Playlist:__\n#{str(int(x + 1))} | {playlist}", value=f"[Go To Playlist]({link})", inline=True)

            if x == amount.playlist: break 

        embed.set_footer(text=f"Requested By {message.author} in #{message.channel}.")
        await message.channel.send("", embed=embed)

    except Exception as e:
        log.log(str(e)) 
