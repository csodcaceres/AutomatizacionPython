# Organizador de Archivos por Extensión (Tkinter)

Este script en Python permite ordenar automáticamente los archivos de una carpeta en subcarpetas según su tipo de extensión, utilizando una interfaz gráfica con `tkinter`. Incluye manejo de errores para mayor robustez.

## 📌 Funcionalidad

Al ejecutar el script:

1. Se abre un cuadro de diálogo para seleccionar la carpeta a ordenar.
2. Se analizan los archivos presentes en esa carpeta.
3. Los archivos se mueven a subcarpetas según su extensión. Si la subcarpeta no existe, se crea automáticamente.
4. Se muestra una ventana informando si el proceso fue exitoso o si hubo errores (por ejemplo, archivos en uso o no encontrados).

## 🧠 Extensiones Soportadas

| Extensión         | Carpeta de destino         |
|-------------------|----------------------------|
| `.jpg`, `.png`, `.jpeg` | Imagenes             |
| `.pdf`            | PDFs                       |
| `.mp4`            | Videos                     |
| `.txt`            | Documentos_txt             |
| `.doc`, `.docx`   | Documentos_Word            |
| `.xlsx`, `.xls`   | Documentos_Excel           |
| `.iso`            | Archivos_ISO               |
| `.pptx`           | Documentos_PowerPoint      |
| `.exe`            | Archivos_exe               |
| `.ipynb`          | Archivos_ipynb             |

## 🚀 Requisitos

- Python 3.x
- Librerías estándar:
  - `os`
  - `shutil`
  - `tkinter` (incluida por defecto con Python)

## ▶️ Ejecución

```bash
python ordenar_archivos_carpetas_tkinter.py
```

Aparecerá una ventana para seleccionar la carpeta. Luego, los archivos serán organizados según su extensión.

## ⚠️ Manejo de Errores

- Si no se selecciona ninguna carpeta, se muestra una advertencia.
- Si algún archivo no se puede mover (por estar en uso o no existir), el error se registra y se muestra al final del proceso.
- Se utiliza `messagebox` para mostrar ventanas emergentes informativas o de error.

## 📂 Ejemplo de Estructura

Antes:

```
📁 Descargas
 ├── imagen.jpg
 ├── informe.pdf
 ├── documento.docx
 ├── video.mp4
```

Después:

```
📁 Descargas
 ├── Imagenes
 │   └── imagen.jpg
 ├── PDFs
 │   └── informe.pdf
 ├── Documentos_Word
 │   └── documento.docx
 ├── Videos
     └── video.mp4
```

## 🧑‍💻 Autor

Oscar Daniel Cáceres
