from random import randint
from os import cwd
from requests import get

#
#By Mirrorz(Aero) :)
#Update 1
#Download Images From a URL

def download_image(url):
    #Current Working Directory
    cwd = getcwd() 
    # Creates a new file with name @ random.
    fname = str(f"{getcwd()}/str"+(randint(1111, 9999))+".png") 
    
    with open(fname, 'wb') as handle:
        response = requests.get(url, stream=True) #Get our file-data.
        if not response.ok:# Main Exception
            #print(f"Failed To Download Image\nResponse:{str(response)}")
            fname = None
            
        #Stitch our data to our file.
        for block in response.iter_content(1024): 
            if not block:
                break
            handle.write(block)
            
    return fname 
