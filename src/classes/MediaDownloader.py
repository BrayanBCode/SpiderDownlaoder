import os
import sys
import tkinter.messagebox
import yt_dlp
import tkinter

ffmpeg_path = os.path.normpath(os.path.join(os.path.abspath(__file__), "..", "src", "ffmpeg", "bin"))
ffmpeg_path = ffmpeg_path.replace("\\", "\\\\")
print(f"ffmpeg_path: {ffmpeg_path}")

class MediaDownloader:
    def __init__(self, vent):
        self.vent = vent

    def pathExists(self, path: str = None):
        if path is None:
            # Obtener la ruta del directorio actual
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # Construir la ruta a la carpeta Downloads
            path = os.path.join(current_dir, "..", "..", "Downloads")
            # Normalizar la ruta
            path = os.path.normpath(path)
        return os.path.exists(path)

    def ensure_download_path(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        download_path = os.path.join(current_dir, "..", "..", "Downloads")
        download_path = os.path.normpath(download_path)

        self.get_exe_path()
        
        if not self.pathExists(download_path):
            os.makedirs(download_path)
        
        return download_path

    def download_video_mp3(self, url: str):
        download_path = self.ensure_download_path()
        ydl_opts = {
            # '--ffmpeg-location': ffmpeg_path,
            'playlist_items': '1',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'verbose':True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                self.SuccesfulDownload()
            except Exception as e:
                print(f"Error en la descarga de mp3: {e}")
                self.DownloadError(e)

    def download_video_mp4(self, url: str):
        download_path = self.ensure_download_path()
        ydl_opts = {
            '--ffmpeg-location': ffmpeg_path,
            'playlist_items': '1',
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s')
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([url])
                self.SuccesfulDownload()
            except Exception as e:
                print(f"Error en la descarga de mp4: {e}")
                self.DownloadError(e)

    def SuccesfulDownload(self):
        
        tkinter.messagebox.showinfo("Descarga Completa", "El video se ha descargado exitosamente.")

    def DownloadError(self, error):
        tkinter.messagebox.showerror("Error de Descarga", f"Se produjo un error durante la descarga: {error}")

    def get_exe_path(self):
        if getattr(sys, 'frozen', False):
            # El script está ejecutándose en un ejecutable
            print(sys._MEIPASS)
            return sys._MEIPASS
        else:
            # El script está ejecutándose en un entorno normal de Python
            return os.path.dirname(os.path.abspath(__file__))