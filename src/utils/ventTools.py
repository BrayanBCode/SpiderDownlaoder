from tkinter import Tk


class ventTools:

    @staticmethod
    def center_window(screen: Tk, width: int, height: int):
        # Establecer el tamaño de la ventana
        screen.geometry(f'{width}x{height}')

        # Obtener el tamaño de la pantalla
        screen_width = screen.winfo_screenwidth()
        screen_height = screen.winfo_screenheight()

        # Calcular la posición x e y para centrar la ventana
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        print(f"Centrando ventana en: {x}, {y}")

        # Establecer la geometría de la ventana con la posición centrada
        screen.geometry(f'{width}x{height}+{x}+{y}')