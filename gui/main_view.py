import tkinter as tk

class App(tk.Tk):
    def _init_(self):
        super()._init_()
        self.title("Detector de Cuentas Falsas")
        self.geometry("800x600")
        # Aquí crearás y mostrarás las vistas