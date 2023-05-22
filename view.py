from PIL import Image

import customtkinter

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

        self.img_cover = customtkinter.CTkLabel(self, image=cover, text="")  # display video cover with a CTkLabel

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x500")
        self.title("YouTube Downloader App")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.frame = MainFrame(master=self)
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()