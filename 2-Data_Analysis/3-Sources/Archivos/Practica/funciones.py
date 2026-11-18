# Importa funciones para trabajar con rutas, carpetas y mover archivos.
import os
import shutil

# Importa las categorias y extensiones configuradas en variables.py.
from variables import categorias, tipos_documentos, tipos_imagenes, tipos_software


def clasificar_archivo(nombre_archivo):
    # Obtiene la extension y la pasa a minusculas para comparar sin distinguir mayusculas.
    extension = os.path.splitext(nombre_archivo)[1].lower()
    # Comprueba la extension en cada lista y devuelve su categoria.
    if extension in tipos_imagenes:
        return 'Imagenes'
    if extension in tipos_documentos:
        return 'Documentos'
    if extension in tipos_software:
        return 'Software'
    # Las extensiones no incluidas en las listas van a "Otros".
    return 'Otros'


def obtener_ruta_disponible(ruta_destino):
    # Si el archivo destino no existe, se conserva su nombre original.
    if not os.path.exists(ruta_destino):
        return ruta_destino

    # Separa la carpeta destino del nombre del archivo.
    carpeta, nombre_archivo = os.path.split(ruta_destino)
    # Separa el nombre y la extension para conservarla al cambiar el nombre.
    nombre, extension = os.path.splitext(nombre_archivo)
    # Inicializa el numero que se agregara para evitar sobrescribir.
    contador = 1
    # Busca consecutivamente un nombre que todavia no exista.
    while True:
        # Construye una alternativa, por ejemplo "archivo_1.pdf".
        ruta_candidata = os.path.join(
            carpeta, f'{nombre}_{contador}{extension}'
        )
        # Devuelve la alternativa en cuanto encuentra una ruta libre.
        if not os.path.exists(ruta_candidata):
            return ruta_candidata
        # Prueba con el siguiente numero si la alternativa ya existe.
        contador += 1


def organizar_archivos(ruta_carpeta):
    # Informa claramente si la ruta recibida no existe.
    if not os.path.exists(ruta_carpeta):
        raise FileNotFoundError(f'No existe la carpeta: {ruta_carpeta}')
    # Informa claramente si la ruta existe pero no es una carpeta.
    if not os.path.isdir(ruta_carpeta):
        raise NotADirectoryError(f'La ruta no es una carpeta: {ruta_carpeta}')

    # Crea las carpetas de categorias; no falla si ya estaban creadas.
    for categoria in categorias:
        os.makedirs(os.path.join(ruta_carpeta, categoria), exist_ok=True)

    # Prepara un contador en cero para cada categoria.
    archivos_movidos = {categoria: 0 for categoria in categorias}
    # Recorre los elementos que hay directamente dentro de la carpeta indicada.
    for nombre_archivo in os.listdir(ruta_carpeta):
        # Construye la ruta completa del elemento actual.
        ruta_origen = os.path.join(ruta_carpeta, nombre_archivo)
        # Omite carpetas y otros elementos que no sean archivos.
        if not os.path.isfile(ruta_origen):
            continue

        # Decide la categoria segun la extension del archivo.
        categoria = clasificar_archivo(nombre_archivo)
        # Construye la ruta inicial dentro de la carpeta de su categoria.
        ruta_destino = os.path.join(
            ruta_carpeta, categoria, nombre_archivo
        )
        # Cambia el nombre si ya existe un archivo con ese nombre en destino.
        ruta_destino = obtener_ruta_disponible(ruta_destino)
        # Mueve el archivo a la carpeta correspondiente.
        shutil.move(ruta_origen, ruta_destino)
        # Suma uno al total de archivos movidos para esa categoria.
        archivos_movidos[categoria] += 1

    # Devuelve el resumen de archivos movidos por categoria.
    return archivos_movidos
