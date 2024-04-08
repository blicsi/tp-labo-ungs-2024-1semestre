# Trabajo Práctico Inicial Laboratorio de Construcción de Software

## Índice

1. [Descripción del Proyecto](#descripción-del-proyecto)
3. [Mockups](#mockups)
4. [Comandos para Levantar el Proyecto](#comandos-para-levantar-el-proyecto)

## Descripción del Proyecto
El objetivo principal del trabajo práctico es la construcción de un Chatbot con IA orientado a un tema a elección.

### Chatbot

Nuestro Chatbot está enfocado en el ámbito universitario para facilitarle la vida académica a los estudiantes de la Universidad Nacional de General Sarmiento (UNGS), con funciones como, mostrar ofertas de comisión, brindar información básica sobre las materias, aulas de cursada, fechas de inscripción, entre otra información útil relativa a la universidad. Además de esto, se busca que el Chatbot pueda mantener una conversación con los estudiantes interpretando lo que envían y respondiendo adecuadamente. 

Para llevar a cabo este proyecto, se emplearán diversas herramientas. Utilizaremos el lenguaje de programación Python junto a diversas librerías. Como `aspose.pdf`, que permite la manipulación de archivos PDF de forma eficiente. Ayudándonos a la hora de realizar la conversión de archivos PDF a formato CSV y así poder alimentar a la IA con el uso de los PDF disponibles en la universidad, como el calendario académico, oferta de comisiones, entre otros. La librería pandas, para el análisis y manipulación de los archivos CSV, limpiar y transformar estos datos. Otra librería importante es `pythorch` o `tenserflow` (junto con `keras`), para el aprendizaje automático que nos servirán a la hora de entrenar a esta IA y además nos permitirá utilizando modelados de lenguaje para que pueda mantener una conversación con los estudiantes.

## Mockups
A continuación se muestran unos mockups de una posible vista final del Chatbot construido.

![Mockup](./img/mockup.png)

## Comandos para levantar el proyecto

Se requiere de installar las siguientes librerias para poder lebantar el proyecto.

Chatbot:

  ```bash
   pip install nltk pandas openpyxl dataset
   ```
  ```bash
   pip3 install torch torchvision torchaudio
   ```

Reconocimiento facial:

  ```bash
   pip install opencv-python opencv-contrib-python imutils
   ```
   correr EntrenamientoLBPH.py antes de correr el __main__

  Además de esto, se deben agregar los archivos de la carpeta [Data](https://drive.google.com/drive/folders/1SIC9dvWZ3jCnUubL4nZVDn60-9IRnJwZ) a Reconocimiento/Facial. Y correr en orden los siguientes arcivos: 
  
  1. [CapturandoRostros.py](./ReconocimientoFacial/CapturandoRostros.py) que se utilizará para capturar las imágenes de la persona, ya sea por webcam o video, revisar variable `personName` antes de correr y tener en cuenta la variable `count`, ya que esta definirá la cantidad de imágenes a tomar para entrenar el modelo. La idea no es tomar ni muchas ni muy pocas, ya que puede generar imperfecciones al entrenar o puede tardar mucho el entrenamiento. Después de varias pruebas encontramos que 2000-2500 es un valor óptimo. Se recomienda ir cambiando `count` e ir capturando por partes con distintos fondos y luces (0-1000, 1001-2000, 2001-500).

  2. [EntrenamientoLBPH.py](./ReconocimientoFacial/EntrenamientoLBPH.py) este archivo se encarga del entrenamiento del modelo, generando `modeloLBPH.xml`que es un .xml con el modelo entrenado. Elegimos este y no `FF` o `RF`, ya que `LBPH` es mucho más rápido y trabaja mejor con un volumen de imágenes más grandes.  

  3. [ResconocimientoFacial.py](./ReconocimientoFacial/ResconocimientoFacial.py) finalmente al correr este archivo se prenderá la webcam de la computadora y podremos probar la IA en caso de no contar con webcam, se puede usar un video (ver variable `cap`).