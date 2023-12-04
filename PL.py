import tkinter as tk
from tkinter import ttk
import os
import subprocess

class UnificadorInterfaz:

    
    def __init__(self, root):
        self.root = root
        self.root.title("Unificador de Códigos")

        # Botón para ejecutar Met_grafico.py
        self.btn_met_grafico = ttk.Button(root, text="Ejecutar Met_grafico.py", command=self.ejecutar_met_grafico)
        self.btn_met_grafico.pack(pady=10)

        # Botón para ejecutar mainDosFases.py
        self.btn_main_dos_fases = ttk.Button(root, text="Ejecutar mainDosFases.py", command=self.ejecutar_main_dos_fases)
        self.btn_main_dos_fases.pack(pady=10)

    def ejecutar_met_grafico(self):
        # Ejecutar el script Met_grafico.py
        subprocess.call(["python", "C:\\Users\\PC\\Documents\\Proyectos VisualStudio\\Proyecto-Investigacion-de-Operaciones\\Met_grafico.py"])
        self.ejecutar_script("Met_grafico.py")

    def ejecutar_main_dos_fases(self):
        # Ejecutar el script mainDosFases.py
        subprocess.call(["python", "C:\\Users\\PC\\Documents\\Proyectos VisualStudio\\Proyecto-Investigacion-de-Operaciones\\mainDosFases.py"])
        self.ejecutar_script("mainDosFases.py")




root = tk.Tk()
app = UnificadorInterfaz(root)
root.geometry("400x400")
root.resizable(True, True)
root.mainloop()

