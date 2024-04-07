import tkinter as tk
import ReconocimientoFacial.ResconocimientoFacial
from better_chatbot.chat import get_response, bot_name  

logeo_exitoso=False

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def pantalla_chatbot():
    #root.geometry("800x800")
    root.configure(width=800,height=800)
    btn_login_huella.grid_remove()
    btn_login_facial.grid_remove()
    btn_registrar_huella.grid_remove()
    btn_registrar_rostro.grid_remove()
#--------------------input de texto-----------------------

    # Variable de control para el campo de texto
    texto_variable = tk.StringVar()

    # Crear el campo de texto y vincularlo a la variable de control
    entrada_texto = tk.Entry(root, textvariable=texto_variable, width=30)
    #entrada_texto.grid(row=0, column=0, padx=10, pady=10)

    # Asignar una función que se ejecutará cada vez que el contenido del campo de texto cambie
    #texto_variable.trace_add("write", actualizar_etiqueta)

    # Etiqueta para mostrar el texto ingresado
    etiqueta = tk.Label(root, text="")
    #etiqueta.grid(row=1, column=0, padx=10, pady=10)
    
    """ entrada_de_texto=tk.Entry(root,width=300)
    entrada_de_texto.grid(row=3, column=0, padx=5, pady=5, sticky="ew")
    entrada_de_texto.pack() """


#--------------------------------------------    

def login_huella():
    print("Iniciar sesión con huella digital")

def login_facial():
    print("Iniciar sesión con reconocimiento facial")

def registrar_huella():
    print("Registrar huella digital")

def registrar_rostro():
    print("Registrar rostro")


def crear_ventana_reconocimiento_facial():
    global logeo_exitoso
    logeo_exitoso=ReconocimientoFacial.ResconocimientoFacial.reconocimiento_facial()
    print(logeo_exitoso)
    pantalla_chatbot()
    

# Crear la ventana principal
root = tk.Tk()
root.title("UNGS Helper")

if (not logeo_exitoso):
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
