# Organizador de Archivos por Extensión (Tkinter)

Este script en Python permite ordenar automáticamente los archivos de una carpeta en subcarpetas según su tipo de extensión, utilizando una interfaz gráfica sencilla con `tkinter`.

## 📌 Funcionalidad

Al ejecutar el script:

1. Se abre un cuadro de diálogo para seleccionar la carpeta que deseas ordenar.
2. Se escanean todos los archivos en esa carpeta.
3. Según su extensión, los archivos se mueven a subcarpetas específicas (que se crean automáticamente si no existen).

Por ejemplo:
- Archivos `.jpg`, `.png`, `.jpeg` se moverán a la carpeta `Imagenes`.
- Archivos `.pdf` se moverán a la carpeta `PDFs`.
- Archivos `.docx`, `.doc` se moverán a la carpeta `Documentos_Word`.
- Y así sucesivamente...

## 🧠 Extensiones Soportadas

| Extensión     | Carpeta de destino           |
|---------------|------------------------------|
| `.jpg`, `.png`, `.jpeg` | Imagenes              |
| `.pdf`        | PDFs                         |
| `.mp4`        | Videos                       |
| `.txt`        | Documentos_txt               |
| `.doc`, `.docx` | Documentos_Word            |
| `.xlsx`, `.xls` | Documentos_Excel           |
| `.iso`        | Archivos_ISO                 |
| `.pptx`       | Documentos_PowerPoint        |
| `.exe`        | Archivos_exe                 |
| `.ipynb`      | Archivos_ipynb               |

## 🚀 Requisitos

- Python 3.x
- Librerías estándar:
  - `os`
  - `shutil`
  - `tkinter` (incluida en la mayoría de las instalaciones de Python)

## ▶️ Ejecución

```bash
python ordenar_archivos_carpetas_tkinter.py
```

## 🛠️ Personalización

Puedes agregar nuevas extensiones o modificar las carpetas de destino editando el diccionario `extensiones` en el script.

## 📂 Estructura de Carpetas de Ejemplo

Antes:

📁 Descargas  
 ├── documento.docx  
 ├── imagen.jpg  
 ├── video.mp4  
 ├── informe.pdf  

Después:

📁 Descargas  
 ├── Documentos_Word  
 │   └── documento.docx  
 ├── Imagenes  
 │   └── imagen.jpg  
 ├── Videos  
 │   └── video.mp4  
 ├── PDFs  
     └── informe.pdf  

## 🧑‍💻 Autor

Oscar Daniel Cáceres
