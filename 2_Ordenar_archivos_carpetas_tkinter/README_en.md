# File Organizer by Extension (Tkinter)

This Python script automatically organizes files in a selected folder into subfolders based on their file extensions, using a simple graphical interface with `tkinter`.

## 📌 Functionality

When you run the script:

1. A dialog window appears for selecting the folder you want to organize.
2. All files in the folder are scanned.
3. Based on their extensions, files are moved into specific subfolders (created automatically if they don't exist).

Examples:
- Files with `.jpg`, `.png`, `.jpeg` go to `Imagenes`.
- Files with `.pdf` go to `PDFs`.
- Files with `.docx`, `.doc` go to `Documentos_Word`.
- And so on...

## 🧠 Supported Extensions

| Extension     | Destination Folder           |
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

## 🚀 Requirements

- Python 3.x
- Standard libraries:
  - `os`
  - `shutil`
  - `tkinter` (included in most Python installations)

## ▶️ How to Run

```bash
python ordenar_archivos_carpetas_tkinter.py
```

## 🛠️ Customization

You can add new extensions or modify destination folders by editing the `extensiones` dictionary in the script.

## 📂 Example Folder Structure

Before:

📁 Downloads  
 ├── documento.docx  
 ├── imagen.jpg  
 ├── video.mp4  
 ├── informe.pdf  

After:

📁 Downloads  
 ├── Documentos_Word  
 │   └── documento.docx  
 ├── Imagenes  
 │   └── imagen.jpg  
 ├── Videos  
 │   └── video.mp4  
 ├── PDFs  
     └── informe.pdf  

## 🧑‍💻 Author

Oscar Daniel Cáceres
