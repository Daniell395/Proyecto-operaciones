import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess

class UnificadorInterfaz:

    
    def __init__(self, root):
        self.root = root
        self.root.title("Proyecto de Investigación de Operaciones")
        # Botón para ejecutar Met_grafico.py
        self.btn_met_grafico = ttk.Button(root, text="Método Gráfico.py", command=self.ejecutar_met_grafico)
        self.btn_met_grafico.pack(pady=10)

        # Botón para ejecutar mainDosFases.py
        self.btn_main_dos_fases = ttk.Button(root, text="Método DosFases.py", command=self.ejecutar_main_dos_fases)
        self.btn_main_dos_fases.pack(pady=10)

        self.img = Image.open("C:\\Users\\PC\\Documents\\Proyectos VisualStudio\\Proyecto operaciones\\logo-udistrital.png")  # reemplaza 'ruta_de_la_imagen' con la ruta a tu imagen
        self.img_copy= self.img.copy()

        self.background_image = ImageTk.PhotoImage(self.img)

        self.background = tk.Label(self.root, image=self.background_image)
        self.background.pack(fill=tk.BOTH, expand=True)
        self.background.bind('<Configure>', self._resize_image)


    def ejecutar_met_grafico(self):
        # Ejecutar el script Met_grafico.py
        subprocess.call(["python", "C:\\Users\\PC\\Documents\\Proyectos VisualStudio\\Proyecto operaciones\\Met_grafico.py"])


    def ejecutar_main_dos_fases(self):
        # Ejecutar el script mainDosFases.py
        subprocess.call(["python", "C:\\Users\\PC\\Documents\\Proyectos VisualStudio\\Proyecto operaciones\\Met_DosFases.py"])


    def _resize_image(self,event):
        image = self.img_copy.resize((event.width, event.height))
        self.background_image = ImageTk.PhotoImage(image)
        self.background.configure(image =  self.background_image)


root = tk.Tk()
app = UnificadorInterfaz(root)
root.geometry("300x400")
root.resizable(True, True)
root.mainloop()

