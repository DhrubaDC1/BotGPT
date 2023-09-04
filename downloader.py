from __future__ import unicode_literals
import yt_dlp

def download_yt(fileLink):
    ydl_opts = {
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([fileLink])
