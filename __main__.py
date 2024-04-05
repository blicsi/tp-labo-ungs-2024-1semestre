import tkinter as tk
import ReconocimientoFacial.ResconocimientoFacial

def login_huella():
    print("Iniciar sesión con huella digital")

def login_facial():
    print("Iniciar sesión con reconocimiento facial")

def registrar_huella():
    print("Registrar huella digital")

def registrar_rostro():
    print("Registrar rostro")


def crear_ventana_reconocimiento_facial():
    ReconocimientoFacial.ResconocimientoFacial.reconocimiento_facial()
    
# Crear la ventana principal
root = tk.Tk()
root.title("UNGS Helper")

# Crear un marco para los botones
frame = tk.Frame(root, width=200, height=200)
frame.pack(padx=200, pady=200)

# Crear los botones
btn_login_huella = tk.Button(frame, text="Login con Huella Digital", command=login_huella)
btn_login_huella.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

btn_login_facial = tk.Button(frame, text="Login con Reconocimiento Facial", command=crear_ventana_reconocimiento_facial)
btn_login_facial.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

btn_registrar_huella = tk.Button(frame, text="Registrar Huella", command=registrar_huella)
btn_registrar_huella.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

btn_registrar_rostro = tk.Button(frame, text="Registrar Rostro", command=registrar_rostro)
btn_registrar_rostro.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

# Iniciar el bucle principal de la aplicación
root.mainloop()
