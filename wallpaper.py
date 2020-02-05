import random
import urllib.request
import os
import requests
import json

nm = random.randint(1,7000)
pth = os.getcwd()
# url =  'https://i.picsum.photos/id/{0}/1920/1080.jpg'.format(number)

def getLink(n):
    r = requests.get(f'http://www.splashbase.co/api/v1/images/{n}')
    try:
        url2=json.loads(r.text)['url']
        print(json.loads(r.text)['url'])
        downloader(url2)
    except:
        print(".", end='')
        getLink(random.randint(1,1000))

def downloader(image_url):
    full_file_name = 'image.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)

def change_wallpaper():
    string ="reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d {0}\\image.jpg /f".format(pth)
    os.system(string)
    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
    # os.system("del .\image.jpg")

getLink(nm)
change_wallpaper()