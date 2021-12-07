from __future__ import unicode_literals

try:
    from pytube import YouTube
    import tkinter as tk
    import requests
    import ffmpeg
    from tkinter import messagebox
    import youtube_dl
    import os
    import requests

except NameError:
    print("Error! Module(s) not found!")


# Embedded youtube-dl (refer to https://github.com/ytdl-org/youtube-dl/blob/master/youtube_dl/YoutubeDL.py)


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(download):
    if download['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'c:\output\%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # Download Button
        self.download = tk.Button(text="Download",command=self.audio_download)
        self.download.place(x=200, y=300)

        # Link Input
        url_x = 50
        url_y = 150
        self.url_textbox = tk.Entry(width=50)
        self.url = tk.Label(text="URL:").place(x=url_x, y=url_y)
        self.url_textbox.place(x=url_x+91, y=url_y)

        # Output Directory
        output_x = 50
        output_y = 200
        self.output_directory_textbox = tk.Entry(width=50)
        self.output_directory = tk.Label(text="Output: ").place(x=output_x, y=output_y)
        self.output_directory_textbox.insert(0, "C:/Output")
        self.output_directory_textbox.place(x=output_x+91, y=output_y)

        # Exit Button
        self.exit = tk.Button(text="Exit", command=self.master.destroy)
        self.exit.place(x=450,y=350)

    def audio_download(self):
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([self.url_textbox.get()])
        print("Done converting!")


root = tk.Tk()
root.geometry("500x400")
root.resizable(False, False)
app = Application(master=root)
app.mainloop()

# 1.) Ask for youtube link DONE
# 2.) Download youtube audio DONE
# 3.) Scrape for song title, features, genre, year
# 3a.) If in album, find song number and album cover
# 3b.) If not in album, find song cover
# 4.) Move audio to correct iTunes Media music folder ...\Artist\Album\
# 4a.) If not in album, move to ...\Artist\Unknown Album\
