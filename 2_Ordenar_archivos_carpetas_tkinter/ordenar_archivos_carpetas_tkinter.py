# Importacion de librerias a utilizar
import os
import shutil
from tkinter import Tk, filedialog, messagebox  # Aseguramos importar messagebox

# Ruta donde vamos crear los arrchivos y las carpetas

ventana = Tk()
ventana.withdraw()

try:
    ruta = filedialog.askdirectory(title="Seleccione la carpeta a ordenar: ")

    if not ruta:
        raise Exception("No se seleccionó ninguna carpeta.")

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

    if errores:
        messagebox.showwarning("Proceso Completado con Errores", "\n".join(errores))
    else:
        messagebox.showinfo("Completado", "Archivos ordenados correctamente.")
        
except Exception as e:
    messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")