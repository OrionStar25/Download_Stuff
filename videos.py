from __future__ import unicode_literals
import youtube_dl

url = raw_input("Enter a video/playlist url to be downloaded: ")

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Done!")

# Check https://github.com/rg3/youtube-dl for more information