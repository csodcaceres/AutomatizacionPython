# Importacion de librerias a utilizar
import os
import shutil

# importaos libreria tkinter
from tkinter import Tk, filedialog

# Ruta donde vamos crear los arrchivos y las carpetas
#ruta = "D:/Oscar/PythonClientes/datosParaOdenar"

ventana = Tk()
ventana.withdraw()

ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar: ")


# Creamos un diccionario para poder asociar las extenciones con las 
# carpetas que vamos a crear
extensiones = {

    ".jpg":"Imagenes",
    ".png":"Imagenes",
    ".jpeg":"Imagenes",
    ".pdf":"PDFs",
    ".mp4":"Videos",
    ".txt":"Documentos_txt",
    ".docx":"Documentos_Word",
    ".doc":"Documentos_Word",
    ".xlsx":"Documentos_Excel",
    ".xls":"Documentos_Excel",
    ".iso":"Archivos_ISO",
    ".pptx":"Documentos_PowerPoint",
    ".exe":"Archivos_exe",
    ".ipynb":"Archivos_ipynb"
}

for carpeta in set(extensiones.values()):
    ruta_carpeta = os.path.join(ruta, carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

# Recorremos la lista de archivos
for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)

    if os.path.isfile(ruta_archivo):
        nombre, ext = os.path.splitext(archivo)
        ext = ext.lower()
    
        if ext in extensiones:
            destino = os.path.join(ruta, extensiones[ext], archivo)
            shutil.move(ruta_archivo, destino)

