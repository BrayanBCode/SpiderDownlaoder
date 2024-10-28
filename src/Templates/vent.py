import tkinter
from src.classes.MediaDownloader import MediaDownloader
from src.utils.ventTools import ventTools



class vent(tkinter.Tk):
    def __init__(self):
        super().__init__()
        ventTools.center_window(self, 500, 600)
        self.title("Spider Downloader - By Codu_")
        self.resizable(False, False)

        self.MediaDownloader = MediaDownloader(self)
        self.DownloadPath = self.MediaDownloader.ensure_download_path()
        
        self.bgColor = "#4B4B4B"

        self.configure(bg=self.bgColor)

        self.add_components()

    def add_components(self):
        self.lblTitle = tkinter.Label(self, text="Spider Downloader", font=("Arial", 24), background=self.bgColor, foreground="white")
        self.lblTitle.pack(pady=20)

        self.lblUrl = tkinter.Label(self, text="Ingrese la URL / link del video", background=self.bgColor, foreground="white")
        self.lblUrl.place(x=50, y=100)

        self.txtFieldUrl = tkinter.Entry()
        self.txtFieldUrl.place(x=50, y=120, width=400, height=25)

        self.btnSubmit = tkinter.Button(self, text="Subir", command=self.onSubmitBtnClick)
        self.btnSubmit.place(width=150, height=35, x=175, y=175)

        self.lblEmptyField = tkinter.Label(self, text="Valor invalido o campo vacio", background=self.bgColor, foreground="red")
        self.lblEmptyField.place(x=295, y=100)
        self.lblEmptyField.place_forget()

        # Variable de control para los botones de opción
        self.radio_var = tkinter.StringVar(value="mp3")

        # Botones de opción
        self.mp3 = tkinter.Radiobutton(self, text="mp3", variable=self.radio_var, value="mp3", background=self.bgColor, foreground="white", activebackground=self.bgColor, activeforeground="white", selectcolor="black")
        self.mp3.place(x=50+123, y=150)

        self.mp4 = tkinter.Radiobutton(self, text="mp4", variable=self.radio_var, value="mp4", background=self.bgColor, foreground="white", activebackground=self.bgColor, activeforeground="white", selectcolor="black")
        self.mp4.place(x=150+123, y=150)

    def add_quality_table(self):
        self.tableContainer = tkinter.Frame(self, background=self.bgColor)
        self.tableContainer.place (x=50, y=250, width=400, height=300)

        self.tableContainer.columnconfigure(0, weight=1)
        self.tableContainer.columnconfigure(1, weight=1)
        self.tableContainer.columnconfigure(2, weight=1)

    def onSubmitBtnClick(self):
        URL = self.txtFieldUrl.get()
        FORMAT = self.radio_var.get()

        if URL == "":
            self.lblEmptyField.place(x=295, y=99)
            return
        
        print(f"URL: {URL}, formato: {FORMAT}")
        self.lblEmptyField.place_forget()

        self.getVideo(URL, FORMAT)

    def getVideo(self, url: str, format: str):
        tkinter.messagebox.showinfo("Descargando", "Descargando video, por favor espere...")
        self.MediaDownloader.download_video_mp3(url) if format == "mp3" else self.MediaDownloader.download_video_mp4(url)