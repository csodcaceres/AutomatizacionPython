
# 📁 Organizador de Archivos por Tipo y Fecha

Este script en Python organiza automáticamente archivos dentro de una carpeta especificada según su tipo y la fecha actual. Es útil para mantener directorios limpios y estructurados cronológicamente.

## 🚀 Funcionalidades

- Detecta archivos por extensión y los clasifica en carpetas como `Imagenes`, `Word`, y `Excel`.
- Crea subcarpetas con la fecha actual (`YYYY-MM-DD`) dentro de cada tipo.
- Solo crea carpetas si hay archivos que mover.
- Fácilmente personalizable para soportar más tipos de archivos.

## 📂 Estructura Esperada

```
datosParaOdenar/
├── Imagenes/
│   └── 2025-05-01/
│       ├── foto1.jpg
│       └── imagen.png
├── Word/
│   └── 2025-05-01/
│       └── documento.docx
├── Excel/
│   └── 2025-05-01/
│       └── datos.xlsx
```

## 🧰 Requisitos

- Python 3.x

No se requieren librerías externas adicionales.

## ⚙️ Cómo usar

1. Clona este repositorio o descarga el script `ordenar_archivos_carpetas.py`.
2. Asegúrate de modificar la variable `ruta_principal` con la ruta a tu carpeta de trabajo.
3. Ejecuta el script:

```bash
python ordenar_archivos_carpetas_V2.py
```

Los archivos serán movidos automáticamente a las carpetas correspondientes.

## 📌 Personalización

Puedes modificar el diccionario `extensiones_a_carpetas` en el script para agregar más extensiones o tipos de archivo.

```python
extensiones_a_carpetas = {
    "Imagenes": [".jpg", ".jpeg", ".png"],
    "Word": [".doc", ".docx"],
    "Excel": [".xls", ".xlsx"],
    "PDF": [".pdf"]
}
```

## 👤 Autor

Oscar Daniel Cáceres

## 📝 Licencia

Este proyecto está licenciado bajo la licencia MIT.
