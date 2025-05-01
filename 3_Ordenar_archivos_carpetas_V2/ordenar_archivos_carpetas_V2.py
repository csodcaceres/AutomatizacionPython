import os
import shutil
from collections import defaultdict
from datetime import date

# Ruta principal
ruta_principal = "D:/Oscar/PythonClientes/datosParaOdenar/"

# Asociación de extensiones a carpetas
extensiones_a_carpetas = {
    "Imagenes": [".jpg", ".jpeg", ".png"],
    "Archivos_Word": [".doc", ".docx"],
    "Archivos_Excel": [".xls", ".xlsx"]
}

# Fecha actual en formato YYYY-MM-DD
fecha_hoy = date.today().isoformat()

# Agrupar archivos por carpeta correspondiente
archivos_por_carpeta = defaultdict(list)

for archivo in os.listdir(ruta_principal):
    ruta_archivo = os.path.join(ruta_principal, archivo)

    if os.path.isfile(ruta_archivo):
        _, extension = os.path.splitext(archivo)
        extension = extension.lower()

        for carpeta, extensiones in extensiones_a_carpetas.items():
            if extension in extensiones:
                archivos_por_carpeta[carpeta].append(archivo)
                break

# Crear carpetas y mover archivos a subcarpeta con fecha
for carpeta, archivos in archivos_por_carpeta.items():
    ruta_carpeta_fecha = os.path.join(ruta_principal, carpeta, fecha_hoy)
    os.makedirs(ruta_carpeta_fecha, exist_ok=True)

    for archivo in archivos:
        origen = os.path.join(ruta_principal, archivo)
        destino = os.path.join(ruta_carpeta_fecha, archivo)
        shutil.move(origen, destino)