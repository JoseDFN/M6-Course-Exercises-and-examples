import tkinter as tk

class Frame(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width= 1280, height= 720)
        self.root = root
        self.pack()
        self.config(bg = 'green')