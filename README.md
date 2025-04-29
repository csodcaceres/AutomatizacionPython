# Organizador de Archivos por Tipo

Este script en Python organiza automáticamente archivos dentro de una carpeta especificada, clasificándolos en subcarpetas según su tipo (extensión). Está diseñado para mantener tus directorios limpios y ordenados.

## 📁 Estructura de Carpetas Soportada

El script crea y organiza archivos en las siguientes carpetas:

- `Imagenes` (`.jpg`, `.png`, `.jpeg`)
- `PDFs` (`.pdf`)
- `Videos` (`.mp4`)
- `Documentos_Word` (`.docx`)
- `Documentos_txt` (`.txt`)
- `Documentos_Excel` (✳️ *por agregar*)
- `Archivos_ISO` (`.iso`)
- `Documentos_PowerPoint` (`.pptx`)
- `Archivos_exe` (`.exe`)
- `Archivos_ipynb` (`.ipynb`)

> ⚠️ Nota: La carpeta `Documentos_Excel` se crea pero actualmente no se están moviendo archivos `.xls` o `.xlsx`. Puedes ampliar el script para incluirlos.

## 🚀 ¿Cómo usarlo?

1. **Edita la ruta base** en el script:
   ```python
   ruta = "D:/Oscar/PythonClientes/datosParaOdenar"
   ```
   Asegúrate de que esta ruta exista y contenga los archivos a ordenar.

2. **Ejecuta el script**:
   ```bash
   python ordenar_archivos_carpetas.py
   ```

3. Los archivos serán automáticamente movidos a las subcarpetas correspondientes.

## 🧱 Requisitos

- Python 3.x
- Módulos estándar: `os`, `shutil` (no requiere instalación adicional)

## 🛠 Personalización

Puedes agregar más tipos de archivos simplemente ampliando el bloque condicional en el bucle, por ejemplo:

```python
elif archivo.endswith(".xlsx") or archivo.endswith(".xls"):
    shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, "Documentos_Excel", archivo))
```

## 📄 Licencia

Este proyecto se distribuye bajo la licencia MIT. Puedes modificarlo y reutilizarlo libremente.
