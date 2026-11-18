from pathlib import Path

# Ruta de la carpeta cuyos archivos se van a ordenar.
ruta_descargas = Path.home() / 'Downloads' / 'Descargas prueba'

# Extensiones que se clasificaran como documentos.
tipos_documentos = ('.doc', '.docx', '.txt', '.pdf', '.xls', '.ppt', '.xlsx', '.pptx')

# Extensiones que se clasificaran como imagenes.
tipos_imagenes = ('.jpg', '.jpeg', '.png', '.svg', '.gif')

# Extensiones que se clasificaran como software.
tipos_software = ('.exe', '.py', '.ipynb')

# Nombres de las carpetas destino que se crearan dentro de la carpeta de descargas.
categorias = ('Imagenes', 'Documentos', 'Software', 'Otros')
