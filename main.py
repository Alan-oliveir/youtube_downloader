import os

from PIL import Image

import customtkinter as ctk

import requests
import datetime
from pytube import YouTube

# =============== Constants ================

PATH = os.path.dirname(os.path.realpath(__file__))

# ================ Funtions ================

def search():
    
    global info_video

    # Get Youtube video url
    url = MainFrame.e_url.get()
    yt = YouTube(url)

    # Video informations search
    title = yt.title # Title of video 
    author = yt.author # Get the video author    
    number_views = yt.views # Number of views of video   
    rating = yt.rating # Get the video average rating 
    duration = str(datetime.timedelta(seconds=yt.length)) # Length of the video
    publish_date = yt.publish_date.strftime('%d/%m/%y') # Get the publish date      
    description = yt.description # Description of video     

    # Get and processing of thumbnail
    thumbnail_url = yt.thumbnail_url # cover of the video
    thumbnail = Image.open(requests.get(thumbnail_url, stream=True).raw)
    thumbnail = ctk.CTkImage(light_image=thumbnail, size=(570, 320))

    info_video = {
        'Title': title,
        'Channel': author,
        'Views': number_views,
        'Rating': rating,
        'Duration': duration,
        'Date': publish_date,
        'Thumbnail': thumbnail,        
        'Description': description
    }

    MainFrame.l_title.configure(text="Título: " + info_video["Title"])
    MainFrame.l_channel.configure(text="Canal: " + info_video["Channel"])
    MainFrame.l_views.configure(text="Views: " + str(info_video["Views"]))
    MainFrame.l_date.configure(text="Data: " + info_video["Date"])
    MainFrame.l_duration.configure(text="Duração: " + info_video["Duration"])
    MainFrame.img_thumb.configure(text="", image=info_video["Thumbnail"])
    
    print (info_video)  

def download():

    try:
        ytLink = MainFrame.e_url.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        video.download()
        FrameBottomBar.l_status.configure(text="Concluído", anchor="center")
    
    except:
        FrameBottomBar.l_status.configure(text="Falhou", text_color="red")


def on_progress(stream, chunk, bytes_remaining):

    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    porcentage_completed = bytes_downloaded / total_size * 100
    print(porcentage_completed)


class FrameTitleBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Font object
        font_title = ctk.CTkFont(family="Verdana", size=21, weight="bold")

        # Open image
        app_img = ctk.CTkImage(Image.open(PATH + "/images/app_logo.png"), size=(60,45))
        
        # Add widgets onto the FrameTitleBar
        label_img = ctk.CTkLabel(self, text="", image=app_img)
        label_img.grid(row=0, column=0, padx=(10,5), pady=5, stick="ne")

        label_title = ctk.CTkLabel(self, text="Youtube Downloader App", font=font_title)
        label_title.grid(row=0, column=1, padx=(5,0), pady=5, stick="nse")


class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
               
        # Open image
        img_download = ctk.CTkImage(Image.open(PATH + "/images/download.png"), size=(25, 25))
        img_search = ctk.CTkImage(Image.open(PATH + "/images/search.png"), size=(25, 25))

        # Font object
        font_title = ctk.CTkFont(size=14, weight="bold")
        font_label = ctk.CTkFont(size=13, weight="normal")

        # Add widgets onto the MainFrame        
        self.l_url = ctk.CTkLabel(self, text="Enter URL:", font=font_title)
        self.l_url.grid(row=0, column=0, padx=20, pady=15)
        
        MainFrame.e_url = ctk.CTkEntry(self, width=485) # entry url
        MainFrame.e_url.grid(row=0, column=1, padx=(0, 25), pady=15)
        
        self.b_search = ctk.CTkButton(self, text="Search", width=140, command=search, font=font_title, image=img_search, compound="left")
        self.b_search.grid(row=0, column=2, padx=(20, 20), pady=15)
        
        MainFrame.img_thumb = ctk.CTkLabel(self, image=None, text="Cover", anchor=ctk.NW, width=575, height=325)  # display video thumb with a CTkLabel
        MainFrame.img_thumb.grid(row=2, column=0, rowspan=5, columnspan=2, padx=(20, 20), pady=(15, 30))
        
        self.b_download = ctk.CTkButton(self, text="Baixar", width=140, command=download, font=font_title, height=50, image=img_download, compound="left")
        self.b_download.grid(row=6, column=2, padx=(20, 20), pady=(15, 30))

        # Widgets with video data
        MainFrame.l_title = ctk.CTkLabel(self, text="Título:", font=font_label)
        MainFrame.l_title.grid(row=1, column=0, columnspan=3, padx=20, pady=0, stick="nw")
        
        MainFrame.l_channel = ctk.CTkLabel(self, text="Canal: ", font=font_label)
        MainFrame.l_channel.grid(row=2, column=2, padx=20, pady=15, stick="nw")
        
        MainFrame.l_views = ctk.CTkLabel(self, text="Views: ", font=font_label)
        MainFrame.l_views.grid(row=3, column=2, padx=20, pady=15, stick="nw")
        
        MainFrame.l_date = ctk.CTkLabel(self, text="Data: ", font=font_label)
        MainFrame.l_date.grid(row=4, column=2, padx=20, pady=15, stick="nw")
        
        MainFrame.l_duration = ctk.CTkLabel(self, text="Duração: ", font=font_label)
        MainFrame.l_duration.grid(row=5, column=2, padx=20, pady=15, stick="nw")


class FrameBottomBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Font object
        font_label = ctk.CTkFont(size=14, weight="bold")
        font_status = ctk.CTkFont(size=18, weight="bold")
       
        # Add widgets onto the FrameBottomBar
        l_porcentage = ctk.CTkLabel(self, text="Progresso:", font=font_label)
        l_porcentage.grid(row=0, column=0, padx=(10, 0), pady=5, stick="ne")

        l_porcentage = ctk.CTkLabel(self, text="0%", font=font_label)
        l_porcentage.grid(row=0, column=1, padx=(5, 5), pady=5, stick="ne")

        progress = ctk.CTkProgressBar(self, width=560, height=12)
        progress.set(0)
        progress.grid(row=0, column=2, padx=(5, 0), pady=5, stick="e")

        FrameBottomBar.l_status = ctk.CTkLabel(self, text="", font=font_status)
        FrameBottomBar.l_status.grid(row=0, column=3, padx=20, pady=5)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.geometry("680x580")
        self.title("YouTube Downloader App")

        # configure grid system
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)

        # Add frames to App        
        self.FrameTitleBar = FrameTitleBar(master=self)
        self.FrameTitleBar.grid(row=0, column=0, padx=5, pady=(5, 2), stick="new")

        self.MainFrame = MainFrame(master=self)
        self.MainFrame.grid(row=1, column=0, padx=5, pady=(0, 2), sticky="nsew")

        self.FrameBottomBar = FrameBottomBar(master=self)
        self.FrameBottomBar.grid(row=2, column=0, padx=5, pady=(0, 5), stick="nsew")

app = App()
app.mainloop()