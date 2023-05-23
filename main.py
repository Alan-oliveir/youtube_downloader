from PIL import Image

import os

import customtkinter as ctk

import requests

from pytube import YouTube

import datetime
from datetime import date
import calendar
# import downloader

# Constants
PATH = os.path.dirname(os.path.realpath(__file__))

# ================ Funtions ================

def search():
    
    global thumbnail, info_video

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
    thumbnail = ctk.CTkImage(light_image=thumbnail, size=(280, 200))

    info_video = {
        'Title': title,
        'Channel': author,
        'Views': number_views,
        'Rating': rating,
        'Duration': duration,
        'Date': publish_date,        
        'Description': description
    }

    MainFrame.l_title.configure(text="Título: " + info_video["Title"])
    
    #print (info_video)

    #return (info_video)
    '''img_ = img_.resize((230, 150), Image.ANTIALIAS)
    img_ = ImageTk.PhotoImage(img_)

    global img

    img=img_
    l_image['image']=img

    l_title['text']="Titlo : " + str(title)
    l_view['text']="Views : " + str('{:,}'.format(view))
    l_time['text']="Duracao : " + str(duration)

print(cover)

previousprogress = 0

def on_progress(stream, chunk, bytes_remaining):
    global previousprogress
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining 

    liveprogress = (int)(bytes_downloaded / total_size * 100)
    if liveprogress > previousprogress:
        previousprogress = liveprogress
        print(liveprogress)
        bar.place(x=250, y=120)
        bar['value'] = liveprogress
        janela.update_idletasks()

def download():
    url=e_url.get()
    yt=YouTube(url)

    yt.register_on_progress_callback(on_progress)
    yt.streams.filter(only_audio=False).first().download()


'''

class FrameTitleBar(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        # Font object
        font_title = ctk.CTkFont(family="Verdana", size=24, weight="bold")

        # Open image
        app_img = ctk.CTkImage(Image.open(PATH + "/images/logo.png"), size=(50,50))
        
        # Add widgets onto the FrameTitleBar
        label_img = ctk.CTkLabel(self, text="", image=app_img)
        label_img.grid(row=0, column=0, padx=(10,5), pady=5, stick="ne")

        label_title = ctk.CTkLabel(self, text="Youtube Downloader App", font=font_title)
        label_title.grid(row=0, column=1, padx=(5,0), pady=0, stick="nse")

class MainFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
       
        my_image = ctk.CTkImage(light_image=Image.open("D:\Arquivos\GitHub\youtube_downloader\img-pokemon-list.png"), size=(375, 320))

        font_title = ctk.CTkFont(size=14, weight="bold")
        font_label = ctk.CTkFont(size=13, weight="bold")

        # add widgets onto the frame        
        self.l_url = ctk.CTkLabel(self, text="Enter URL:", font=font_title) # label url
        self.l_url.grid(row=0, column=0, padx=20, pady=15)
        MainFrame.e_url = ctk.CTkEntry(self, width=350) # entry url
        MainFrame.e_url.grid(row=0, column=1, padx=0, pady=15)
        self.b_search = ctk.CTkButton(self, text="Search", width=140, command=search, font=font_title)
        self.b_search.grid(row=0, column=2, padx=(20, 20), pady=15)
        self.img_thumb = ctk.CTkLabel(self, image=my_image, text="")  # display video cover with a CTkLabel
        self.img_thumb.grid(row=2, column=0, rowspan=5, columnspan=2, padx=(20, 20), pady=(15, 30))

        # widgets with video data
        MainFrame.l_title = ctk.CTkLabel(self, text="Título", font=font_title)
        MainFrame.l_title.grid(row=1, column=0, columnspan=3, padx=20, pady=0)
        self.l_title = ctk.CTkLabel(self, text="Canal: ", font=font_label)
        self.l_title.grid(row=2, column=2, padx=20, pady=15)
        self.l_title = ctk.CTkLabel(self, text="Views: ", font=font_label)
        self.l_title.grid(row=3, column=2, padx=20, pady=15)
        self.l_title = ctk.CTkLabel(self, text="Data: ", font=font_label)
        self.l_title.grid(row=4, column=2, padx=20, pady=15)
        self.l_title = ctk.CTkLabel(self, text="Duração: ", font=font_label)
        self.l_title.grid(row=5, column=2, padx=20, pady=15)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.geometry("680x580")
        self.title("YouTube Downloader App")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = MainFrame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()