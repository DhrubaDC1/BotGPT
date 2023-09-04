from moviepy.editor import VideoFileClip


def convert_webm_to_mp4(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    video_clip.write_videofile(output_path, codec="libx264")

def convert_webm_to_mp3(input_path, output_path):
    video_clip = VideoFileClip(input_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_path)
