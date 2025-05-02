# Organizador de Archivos por Tipo y Fecha

Este script en Python permite ordenar automáticamente los archivos de una carpeta seleccionada, clasificándolos por tipo de archivo (por su extensión) y moviéndolos a subcarpetas organizadas por fecha. La interfaz gráfica para seleccionar la carpeta es provista por `Tkinter`.

## 📁 Estructura de Organización

Los archivos se moverán a subcarpetas con la siguiente estructura:

```
<carpeta_origen>/
├── Imagenes/
│   └── 2025-05-02/
│       ├── imagen1.jpg
│       └── imagen2.png
├── PDFs/
│   └── 2025-05-02/
│       └── archivo.pdf
...
```

## 🧰 Tipos de Archivos Soportados

El script reconoce y organiza los siguientes tipos de archivos:

- `.jpg`, `.jpeg`, `.png` → Imagenes
- `.pdf` → PDFs
- `.mp4` → Videos
- `.txt` → Documentos_txt
- `.docx`, `.doc` → Documentos_Word
- `.xlsx`, `.xls` → Documentos_Excel
- `.pptx` → Documentos_PowerPoint
- `.iso` → Archivos_ISO
- `.exe` → Archivos_exe
- `.ipynb` → Archivos_ipynb

## ▶️ Cómo Usarlo

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el script:
   ```bash
   python ordenar_archivos_carpetas_tkinter_v2.py
   ```
3. Se abrirá una ventana para que selecciones la carpeta que deseas organizar.
4. Los archivos serán movidos automáticamente a subcarpetas según su tipo y la fecha actual.
5. Al finalizar, se mostrará un mensaje indicando que el proceso fue completado con éxito.

## ✅ Instrucciones para Ejecutarlo

1. Descargá el archivo `ordenar_archivos_carpetas_tkinter_v2.py`.
2. Abrí una terminal y navegá a la carpeta donde guardaste el archivo.
3. Ejecutá el script con el siguiente comando:
   ```bash
   python ordenar_archivos_carpetas_tkinter_v2.py
   ```
4. Seleccioná la carpeta que deseás organizar cuando se abra la ventana.

## 🛑 Manejo de Errores

- Si no se selecciona ninguna carpeta, se mostrará un mensaje de error.
- Cualquier error durante la ejecución será mostrado en una ventana emergente.

## 📦 Requisitos

- Python 3
- Tkinter (incluido por defecto en Python)

## 📄 Licencia

MIT License
