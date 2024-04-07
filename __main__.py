import tkinter as tk
import sys
import ReconocimientoFacial.ResconocimientoFacial
from better_chatbot.chat import get_response

logeo_exitoso=False

def cerrar_ventana_secundaria():
    sys.exit()

def pantalla_chatbot():
    root.withdraw()  # Ocultar la ventana principal
    ventana_secundaria.deiconify()
    ventana_secundaria.geometry("800x600")  # Cambiar el tamaño de la ventana secundaria a 400x300 
    ventana_secundaria.protocol("WM_DELETE_WINDOW", cerrar_ventana_secundaria)  

def login_huella():
    print("Iniciar sesión con huella digital")

def login_facial():
    print("Iniciar sesión con reconocimiento facial")

def registrar_huella():
    print("Registrar huella digital")

def registrar_rostro():
    print("Registrar rostro")

def obtener_texto():
    texto = entrada_texto.get()
    respuesta = get_response(texto)
    area_texto.config(state="normal")  # Habilitar la edición del área de texto
    area_texto.insert(tk.END,"vos: "+texto + "\n\n")  # Insertar el texto en el área de texto
    area_texto.insert(tk.END,f"{respuesta}\n\n")  # Insertar el texto en el área de texto
    area_texto.config(state="disabled")  # Deshabilitar la edición del área de texto}
    entrada_texto.delete(0, tk.END)  # Vaciar el campo de entrada de texto


def crear_ventana_reconocimiento_facial():
    global logeo_exitoso
    logeo_exitoso=ReconocimientoFacial.ResconocimientoFacial.reconocimiento_facial()
    print(logeo_exitoso)
    if logeo_exitoso:
        print("logeo exitoso")
        pantalla_chatbot()
    else:
        print("logeo fallido")
    #pantalla_chatbot()
    
def mostrar_ventana_principal():
    ventana_secundaria.withdraw()  # Ocultar la ventana secundaria
    root.deiconify()  # Mostrar la ventana principal


# Crear la ventana principal
root = tk.Tk()
root.title("UNGS Helper")

#if (not logeo_exitoso):
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

btn_admin = tk.Button(frame, text="Saltear login", command=pantalla_chatbot)
btn_admin.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

# Crear la ventana secundaria y ocultarla inicialmente
ventana_secundaria = tk.Toplevel(root)
ventana_secundaria.title("Ventana Secundaria")
ventana_secundaria.withdraw()

# Botón para volver a la ventana principal
boton_volver = tk.Button(ventana_secundaria, text="cerrar sesion", command=mostrar_ventana_principal)
boton_volver.pack()

# Crear una entrada de texto
entrada_texto = tk.Entry(ventana_secundaria,width=90)
entrada_texto.pack(side="bottom", fill="x", padx=10, pady=10)

# Botón para obtener el texto ingresado
boton = tk.Button(ventana_secundaria, text="ingresar codigo de materia, nombre de materia, dia de cursada y comision:", command=obtener_texto)
boton.pack(side="bottom", padx=10, pady=10)

# Crear un contenedor para el área de texto con un color de fondo
contenedor_texto = tk.Frame(ventana_secundaria, bg="lightgray")
contenedor_texto.pack(fill="both", expand=True)

# Crear un área de texto dentro del contenedor
area_texto = tk.Text(contenedor_texto, bg="white", wrap="word", state="disabled")
area_texto.pack(side="left", fill="both", expand=True)

# Crear una barra de desplazamiento para el área de texto
scrollbar = tk.Scrollbar(contenedor_texto, command=area_texto.yview)
scrollbar.pack(side="right", fill="y")
area_texto.config(yscrollcommand=scrollbar.set)

# Iniciar el bucle principal de la aplicación
root.mainloop()
