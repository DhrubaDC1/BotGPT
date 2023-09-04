from moviepy.editor import VideoFileClip


def convert_webm_to_mp4():
    video_clip = VideoFileClip('vid.webm')
    video_clip.write_videofile('vid.mp4', codec="libx264")

def convert_webm_to_mp3(input, output):
    video_clip = VideoFileClip(input)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output)
