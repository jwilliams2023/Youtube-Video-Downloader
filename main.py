from pytube import YouTube
import tkinter as tk
from tkinter import simpledialog
import os
import sys

#tinker  simple gui setup
root = tk.Tk()
root.withdraw()
video_url = simpledialog.askstring("Input", "Enter the YouTube video URL:")
download_dir = os.path.join("/Users/Joseph/Downloads/spotify/spotify")
def download_audio(video_url):
    try:
        yt = YouTube(video_url)
        audio_filename = os.path.join(f"downloads/{yt.title}_audio.mp3")
        audio_stream = yt.streams.filter(only_audio=True).first()
        print("Downloading audio:", yt.title)
        if not os.path.exists(download_dir):
            os.makedirs(download_dir)
        audio_stream.download(output_path=download_dir, filename=os.path.basename(audio_filename))
        print("Audio download complete")
        return audio_filename
    except Exception as e:
        print("Error:", str(e))
        return None

if video_url:
    # Download audio
    audio_file = download_audio(video_url)

    if audio_file:
        print("Audio downloaded successfully!")

        # You can perform further actions or use the downloaded file as needed
    else:
        print("Error downloading audio.")
else:
    print("Invalid URL.")
