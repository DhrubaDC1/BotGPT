from __future__ import unicode_literals
import yt_dlp
from convert import *

ydl_opts = {
    'outtmpl': 'vid',  # Specify the output filename
}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])
convert_webm_to_mp4('vid.webm', 'vid.mp4')
convert_webm_to_mp3('vid.webm', 'vid.mp3')
