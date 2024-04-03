import pandas as pd

# Ruta del archivo Excel
archivo_excel = 'better_chatbot/COMISIONES.xlsx'  # Reemplaza 'ejemplo.xlsx' con la ruta de tu propio archivo Excel

# Configurar opciones de visualización
# pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)

# Leer el archivo Excel
datos_excel = pd.read_excel(archivo_excel)

# Mostrar los datos leídos
print("Datos leídos del archivo Excel:")
print(datos_excel)

# Guardar los datos en un archivo CSV separado por ";"
datos_excel.to_csv('better_chatbot/COMISIONES.csv', sep=';', index=False, encoding='latin1')

print("Se ha guardado el archivo CSV correctamente.")