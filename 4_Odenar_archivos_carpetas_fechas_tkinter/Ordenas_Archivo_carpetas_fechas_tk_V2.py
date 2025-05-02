
# Importacion de librerias a utilizar
import os
import shutil
from tkinter import Tk, filedialog, messagebox
from collections import defaultdict
from datetime import date

# Ruta donde vamos crear los arrchivos y las carpetas
ventana = Tk()
ventana.withdraw()

try:
    ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar:")

    if not ruta:
        raise Exception("No se seleccionó ninguna carpeta.")

    # Diccionario de extensiones
    extensiones = {
        ".jpg": "Imagenes",
        ".png": "Imagenes",
        ".jpeg": "Imagenes",
        ".pdf": "PDFs",
        ".mp4": "Videos",
        ".txt": "Documentos_txt",
        ".docx": "Documentos_Word",
        ".doc": "Documentos_Word",
        ".xlsx": "Documentos_Excel",
        ".xls": "Documentos_Excel",
        ".iso": "Archivos_ISO",
        ".pptx": "Documentos_PowerPoint",
        ".exe": "Archivos_exe",
        ".ipynb": "Archivos_ipynb"
    }

    fecha_hoy = date.today().isoformat()
    archivos_por_tipo = defaultdict(list)

    # Clasificar archivos por tipo
    for archivo in os.listdir(ruta):
        ruta_archivo = os.path.join(ruta, archivo)
        if os.path.isfile(ruta_archivo):
            _, ext = os.path.splitext(archivo)
            ext = ext.lower()
            if ext in extensiones:
                carpeta = extensiones[ext]
                archivos_por_tipo[carpeta].append(archivo)

    # Crear carpetas solo si hay archivos, incluyendo subcarpeta con fecha
    for carpeta, archivos in archivos_por_tipo.items():
        ruta_carpeta_fecha = os.path.join(ruta, carpeta, fecha_hoy)
        os.makedirs(ruta_carpeta_fecha, exist_ok=True)

        for archivo in archivos:
            origen = os.path.join(ruta, archivo)
            destino = os.path.join(ruta_carpeta_fecha, archivo)
            shutil.move(origen, destino)

    messagebox.showinfo("Completado", "Archivos ordenados correctamente.")

except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")
