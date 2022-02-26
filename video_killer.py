import ffmpeg
import os
import subprocess
from pytube import YouTube

def get_length(filename):
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=duration", "-of",
                             "default=noprint_wrappers=1:nokey=1", filename],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    return float(result.stdout)
Video = input("What is the direct path/Youtbe link to the video you want to kill?\nLinux Ex: I HATE THIS BIRD.mp4\nWindows Ex: C/Users/isaac/Videos/I HATE THIS BIRD.mp4\n")
Name = input("What do you want the video to be named?\n")
if "https://" in Video:
    yt = YouTube(Video)
    yt.streams.filter(file_extension='mp4')
    YouTube(Video).streams.first().download(filename='video.mp4')
    Video = "video.mp4"
#Goodness = input("How good do you want the video to be? This must be an integer\n")
size = os.path.getsize(Video) 
length = get_length(Video)
stream = ffmpeg.input(Video)
stream = ffmpeg.output(stream, f"{Name}.mp4",video_bitrate=size/length/2.1,audio_bitrate=size/length/3)
try:
  ffmpeg.run(stream)
except:
  ffmpegdir = input("You don't seem to have ffmpeg set as a PATH enviornment variable. Where is your ffmpeg.exe?\n")
  os.environ['path'] = ffmpegdir
finally:
  pass
os.open(f"{Name}.mp4", os.O_RDWR)