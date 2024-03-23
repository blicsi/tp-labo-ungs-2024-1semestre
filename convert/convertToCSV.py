from asposepdf import Document

pdf_path = "Oferta-1-2024.pdf"
extractText = ""

doc = Document(pdf_path)

# Extraer texto por paginas
for page in doc.pages:
    extractText += page.get_text()

# Dividir el texto en líneas
lines = extractText.split('\n')

# Dividir cada línea en columnas para el formato CSV
filas = [line.split(',') for line in lines]

# Escribir el contenido
csv_path = "output.csv"
with open(csv_path, 'w') as f:
    for fila in filas:
        f.write(','.join(fila) + '\n')

print(f"Se ha guardado el archivo CSV en: {csv_path}")
