import tkinter as tk


class DisplayGrid(tk.Frame):
    def __init__(self, master: tk.Tk):
        super().__init__()
        self.master = master
        self.values = []
        self.grid()

    def grid(self):
        self.grid_container = tk.Frame(self.master)
        self.grid_container.place(x=50, y=250, width=400, height=300)

        self.grid_container.columnconfigure(0, weight=1)
        self.grid_container.columnconfigure(1, weight=1)
        self.grid_container.columnconfigure(2, weight=1)

    def add_values(self, data):
        self.values = data
        
        for 


        