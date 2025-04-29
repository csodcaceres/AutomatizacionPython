import os
import shutil

# Ruta donde vamos crear los arrchivos y las carpetas
ruta = "D:/Oscar/PythonClientes/datosParaOdenar"

# Crear las carpetas en destino en caso de que no existen
tipos = ["Imagenes", "PDFs", "Videos", "Documentos_Word", "Documentos_txt", 
         "Documentos_Excel", "Archivos_ISO", "Documentos_PowerPoint", "Archivos_exe",
         "Archivos_ipynb"]

for carpeta in tipos:
    ruta_carpeta = os.path.join(ruta, carpeta)

    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

for archivo in os.listdir(ruta):

    if archivo.endswith(".jpg") or archivo.endswith(".png") or archivo.endswith(".jpeg"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Imagenes", archivo))

    elif archivo.endswith(".pdf"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "PDFs", archivo))
    
    elif archivo.endswith(".mp4"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Videos", archivo))

    elif archivo.endswith(".docx"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Word", archivo))

    elif archivo.endswith(".txt"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_txt", archivo))

    elif archivo.endswith(".iso"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Archivos_ISO", archivo))

    elif archivo.endswith(".pptx"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_PowerPoint", archivo))

    elif archivo.endswith(".exe"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Archivos_exe", archivo))

    elif archivo.endswith(".ipynb"):
        shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Archivos_ipynb", archivo))