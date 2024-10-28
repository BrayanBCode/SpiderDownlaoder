try:
    import sys
    import os
    import traceback

    # Obtener la ruta completa del directorio 'SpiderDownloader'
    root = os.path.dirname(os.path.dirname(__file__))
    print(f"Iniciando ejecución en la carpeta: {os.path.basename(root)}")
    
    # print(f"Test path: {os.path.join(os.path.abspath(__file__), "..", "ffmpeg", "bin", "ffmpeg.exe")}")

    # Agregar el directorio 'SpiderDownloader' al path de ejecución
    sys.path.append(root)

    from src.Templates.vent import vent

    # if __name__ == "__main__":
    #     app = SpiderDownloader()
    #     app.mainloop()

    if __name__ == "__main__":

            app = vent()
            app.mainloop()
except Exception as e:
    print("Ocurrió un error durante la ejecución:")
    print(traceback.format_exc())
    input("Presiona Enter para salir...")
