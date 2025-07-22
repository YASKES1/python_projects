from pytube import YouTube
from sys import argv
#youtube video downloader


path="./download"

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download(path)


