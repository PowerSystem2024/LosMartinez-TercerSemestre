import os

class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    @staticmethod
    def agregar_pelicula(pelicula):
        with open(CatalogoPeliculas.ruta_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(str(pelicula) + '\n')

    @staticmethod
    def listar_peliculas():
        with open(CatalogoPeliculas.ruta_archivo, 'r', encoding='utf-8') as archivo:
            print('\nPelículas en el catálogo:')
            print(archivo.read())

    @staticmethod
    def eliminar():
        os.remove(CatalogoPeliculas.ruta_archivo)
        print('\nArchivo eliminado.')