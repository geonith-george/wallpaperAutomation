import random
import urllib.request
import os

number = random.randint(1,1000)
url =  'https://i.picsum.photos/id/{0}/1920/1080.jpg'.format(number)
pth = os.getcwd()

def downloader(image_url):
    full_file_name = 'image.jpg'
    urllib.request.urlretrieve(image_url,full_file_name)

def change_wallpaper():
    string ="reg add \"HKEY_CURRENT_USER\\Control Panel\\Desktop\" /v Wallpaper /t REG_SZ /d {0}\\image.jpg /f".format(pth)
    os.system(string)
    print(string)
    os.system("RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters")
    os.system("del .\image.jpg")
try:
    downloader(url)
    change_wallpaper()
except:
    pass