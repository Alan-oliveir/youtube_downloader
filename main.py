from PIL import Image

import customtkinter

import requests

from pytube import YouTube

import datetime
#import calendar
# import downloader

# ================ Funtions ================

def search():
    
    global thumbnail

    # Get Youtube video url
    url = MainFrame.e_url.get()
    yt = YouTube(url)

    # Video informations search
    title = yt.title # Title of video 
    author = yt.author # Get the video author    
    view = yt.views # Number of views of video   
    rating = yt.rating # Get the video average rating 
    duration = str(datetime.timedelta(seconds=yt.length)) # Length of the video
    publish_date = yt.publish_date # Get the publish date   
    description = yt.description # Description of video 

    # Get and processing of thumbnail
    thumbnail_url = yt.thumbnail_url # cover of the video
    thumbnail = Image.open(requests.get(thumbnail_url, stream=True).raw)
    thumbnail = customtkinter.CTkImage(thumbnail, size=(280, 200))
    
    #img_ = img_.resize((230, 150), Image.ANTIALIAS)
    #img_ = ImageTk.PhotoImage(img_)

    #global img

    #img=img_
    #l_image['image']=img

    '''l_title['text']="Titlo : " + str(title)
    l_view['text']="Views : " + str('{:,}'.format(view))
    l_time['text']="Duracao : " + str(duration)'''

#print(cover)

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


class MainFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame        
        self.l_url = customtkinter.CTkLabel(self, text="Enter URL:") # label url
        self.l_url.grid(row=0, column=0, padx=20, pady=15)
        self.e_url = customtkinter.CTkEntry(self, width=320) # entry url
        self.e_url.grid(row=0, column=1, padx=0, pady=15)
        self.b_search = customtkinter.CTkButton(self, text="Search", width=100)
        self.b_search.grid(row=0, column=2, padx=(20, 20), pady=15)

        self.img_thumb = customtkinter.CTkLabel(self, image=thumbnail, text="")  # display video cover with a CTkLabel

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("YouTube Downloader App")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = MainFrame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

search()

app = App()
app.mainloop()