# Importa la funcion que organiza la carpeta.
from funciones import organizar_archivos

# Importa la ruta configurada en variables.py.
from variables import ruta_descargas


def ejecutar_programa():
    # Organiza los archivos y obtiene el total movido por categoria.
    archivos_movidos = organizar_archivos(ruta_descargas)
    # Muestra cuantos archivos se movieron a cada carpeta.
    for categoria, cantidad in archivos_movidos.items():
        print(f'{categoria}: {cantidad} archivo(s) movido(s)')


# Ejecuta el programa solo cuando este archivo se ejecuta directamente.
if __name__ == '__main__':
    ejecutar_programa()
