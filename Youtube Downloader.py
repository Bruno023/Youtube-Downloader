import pytube 
import urllib.request
import os
import re
from folder import create_folder

def menu():
    print("*"*30)
    print("Que cancion queres descargar")
    print("E. Salir")
    print("*"*30)

    i = input(":")

    if i == "e" or i=="E":
        return False
    else:
        song = i.replace(' ','')
        return song

def make_url(song):
    if song:
        r = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={song}")
        id_video = re.findall(r"watch\?v=(\S{11})", r.read().decode())[0]
        url = "https://www.youtube.com/watch?v="+ id_video

        return url
    else:
       song = menu()

def download(url):
    audio = pytube.YouTube(url)

    create_folder("song")
    video = audio.streams.filter(only_audio=True).first()
    video.download("song")

while True:
    try:
        song=menu()
        if song:
            url = make_url(song)
            download(url)
        else:
            break
    except KeyboardInterrupt:
        print("Rompi")
        break