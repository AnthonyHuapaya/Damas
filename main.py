import tkinter as tk

root = tk.Tk()
root.title("Hola Mundo")
root.geometry("400x200")

label = tk.Label(root, text="¡Interfaz en Tkinter lista!", font=("Arial", 14))
label.pack(pady=50)

root.mainloop()