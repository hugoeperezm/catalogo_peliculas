import tkinter as tk
from cliente.gui_app import Frame, barra_menu
import os


def main():
    # Clase que crea la interfaz
    root = tk.Tk()
    root.title('Catalogo peliculas')
    # root.iconbitmap('img/logo_python.ico')
    # print(os.path.realpath(__file__))
    # root.resizable(0, 0)  # Se comenta temporalmente mientras se diseña
    barra_menu(root)

    # Se reemplaza estas instrucciones por el modulo creado de gui_app.py
    # frame = tk.Frame(root)
    # frame.pack()
    # frame.config(width=480, height=320, bg='green')
    app = Frame(root=root)

    # como ya se está usando el Frame desde el modulo Cliente, no usaremos root.mainloop()
    # sino app.mainloop()
    app.mainloop()


if __name__ == '__main__':
    main()