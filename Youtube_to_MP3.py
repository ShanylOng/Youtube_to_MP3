import time
import youtube_dl

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

vidlist = ["place", "your", "links", "here"]

i = 1
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    for vid in vidlist:
        ydl.download([vid])
        print("Downloaded " + str(i) + " out of " + str(len(vidlist)) + " files.")
        i += 1
