import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

# Crear la ventana principal con el tema 'vistaero'
root = ThemedTk(theme="vistaero")

# Establecer el título de la ventana
root.title("Inflación")

# Obtener las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calcular el tamaño de la ventana como el 40% de la pantalla
window_width = int(screen_width * 0.4)
window_height = int(screen_height * 0.4)

# Centrar la ventana en la pantalla
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)

# Establecer la geometría de la ventana
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")


# Función para abrir el cuadro de diálogo de selección de archivos
def open_file_dialog():
    filename = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
    print(f"Archivo seleccionado: {filename}")


# Crear el botón con estilo personalizado
button = ttk.Button(root, text="Seleccionar tabla", command=open_file_dialog)
button.pack(padx=10, pady=5, ipadx=10, ipady=5)

# Ejecutar la aplicación
root.mainloop()
