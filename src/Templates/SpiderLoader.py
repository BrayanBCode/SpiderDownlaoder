import tkinter as tk
from PIL import Image, ImageTk

class SpiderDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Spider Loader - By Codu_")
        self.geometry("500x600")
        self.center_window(500, 600)
        self.resizable(False, False)
        
        self.bgColor = "#4B4B4B"
        self.gridColor = "grey"
        self.lastClickedRow = None

        self.grid_values = {}

        self.configure(bg=self.bgColor)

        self.add_entry_components()
        self.add_grid_components()

    def center_window(self, width, height):
        # Obtener el tamaño de la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        # Establecer la geometría de la ventana
        self.geometry(f'{width}x{height}+{x}+{y}')

    def add_entry_components(self):
        self.lblTitle = tk.Label(self, text="Spider Downloader", font=("Arial", 24), background=self.bgColor, foreground="white")
        self.lblTitle.pack(pady=20)

        self.lblUrl = tk.Label(self, text="Ingrese la URL / link del video", background=self.bgColor, foreground="white")
        self.lblUrl.place(x=50, y=100)

        self.txtFieldUrl = tk.Entry()
        self.txtFieldUrl.place(x=50, y=120, width=400, height=25)

        self.btnSubmit = tk.Button(self, text="Subir", command=self.onSubmitBtnClick)
        self.btnSubmit.place(width=150, height=35, x=175, y=165)

        self.lblEmptyField = tk.Label(self, text="Valor invalido o campo vacio", background=self.bgColor, foreground="red")
        self.lblEmptyField.place(x=295, y=100)
        self.lblEmptyField.place_forget()

    def add_grid_components(self, data: list[dict]):
        # Crear un Frame para el grid
        self.gridContainer = tk.Frame(self, background=self.bgColor)
        self.gridContainer.place(x=50, y=250, width=400, height=300)

        # Configurar las columnas del grid
        self.gridContainer.columnconfigure(0, weight=1)
        self.gridContainer.columnconfigure(1, weight=1)
        self.gridContainer.columnconfigure(2, weight=1)


        # Agregar encabezados de columna
        self.lblTitleHeader = tk.Label(self.gridContainer, text="Título", background=self.gridColor, foreground="white", bd=1, relief="solid")
        self.lblTitleHeader.grid(row=0, column=0, sticky="nsew")

        self.lblDurationHeader = tk.Label(self.gridContainer, text="Duración", background=self.gridColor, foreground="white", bd=1, relief="solid")
        self.lblDurationHeader.grid(row=0, column=1, sticky="nsew")

        self.lblQualityHeader = tk.Label(self.gridContainer, text="Calidad", background=self.gridColor, foreground="white", bd=1, relief="solid")
        self.lblQualityHeader.grid(row=0, column=2, sticky="nsew")

        # Datos de ejemplo
        # example_data = [
        #     {"title": "Ejemplo de Título 1", "duration": "10:00", "quality": "480p"},
        #     {"title": "Ejemplo de Título 2", "duration": "12:00", "quality": "1080p"},
        #     {"title": "Ejemplo de Título 2", "duration": "12:00", "quality": "1080pHD"},
        #     {"title": "Ejemplo de Título 2", "duration": "12:00", "quality": "240p"},
        #     {"title": "Ejemplo de Título 3", "duration": "15:00", "quality": "480p"}
        # ]

    def load_data_grid(self, data: list[dict]):
        for i, data in enumerate(data, start=1):
            self.grid_values[i] = {
                'title': tk.Label(self.gridContainer, text=data["title"], background=self.gridColor, foreground="white", bd=1, relief="solid"),
                'duration': tk.Label(self.gridContainer, text=data["duration"], background=self.gridColor, foreground="white", bd=1, relief="solid"),
                'quality': tk.Label(self.gridContainer, text=data["quality"], background=self.gridColor, foreground="white", bd=1, relief="solid")
            }
            self.grid_values[i]['title'].grid(row=i, column=0, sticky="nsew")
            self.grid_values[i]['duration'].grid(row=i, column=1, sticky="nsew")
            self.grid_values[i]['quality'].grid(row=i, column=2, sticky="nsew")

            # Configurar las filas del grid para que se expandan
            self.gridContainer.rowconfigure(i, weight=100)

            # Agregar evento de clic a las celdas
            for widget in self.grid_values[i].values():
                widget.bind("<Button-1>", self.on_row_click)

    def onSubmitBtnClick(self):
        if not self.txtFieldUrl.get():
            self.lblEmptyField.place(x=295, y=100)  # Mostrar el label
        else:
            self.lblEmptyField.place_forget()  # Ocultar el label
            print(self.txtFieldUrl.get())

    def on_row_click(self, event):
        # Obtener el widget que fue clicado
        clicked_widget = event.widget

        # Encontrar la fila correspondiente al widget clicado
        for row, widgets in self.grid_values.items():
            if clicked_widget in widgets.values():
                title = widgets['title'].cget("text")
                duration = widgets['duration'].cget("text")
                quality = widgets['quality'].cget("text")
                print(f"Fila {row} - Título: {title}, Duración: {duration}, Calidad: {quality}")
                break