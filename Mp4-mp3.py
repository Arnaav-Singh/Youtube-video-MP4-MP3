from pytube import YouTube
from moviepy.editor import *
import os, shutil

def get_mp3():
    url = input("Enter a youtube link:  ")
    output = input("What format would you like it in (wav/mp3?:  ")
    print("Converting")

    mp4 = YouTube(url).streams.get_highest_resolution().download()
    mp3 = mp4.split(".mp4", 1)[0] + f".{output}"

    video_clip = VideoFileClip(mp4)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(mp3)

    audio_clip.close()
    video_clip.close()
get_mp3()
