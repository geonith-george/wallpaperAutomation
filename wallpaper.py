import random
import urllib.request
import os
import requests
import json


pth = os.getcwd()
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

def splashbase():
    nm = random.randint(1,7000)
    getLink(nm)
    change_wallpaper()

def picsum():
    nm = random.randint(1,1200)
    url =  'https://i.picsum.photos/id/{0}/1920/1080.jpg'.format(nm)
    print(url)
    downloader(url)
    change_wallpaper()

def run():
    v = int(input('1. splashbase\n2. picsum (recommended)\n'))
    os.system("cls")
    if v == 1:
        splashbase()
    elif v == 2:
        picsum()
    else:
        print("try again2")

while(True):
    run()
    v = input("1. Press enter to continue\n2. q to quit")
    os.system("cls")
    if v == 'q':
        break