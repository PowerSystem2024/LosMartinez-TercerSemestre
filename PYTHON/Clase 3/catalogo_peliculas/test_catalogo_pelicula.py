from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas

def menu():
    opcion = None
    while opcion != '4':
        print('\n-----------------------')
        print('Opciones:')
        print('1) Agregar película')
        print('2) Listar películas')
        print('3) Eliminar archivo de películas')
        print('4) Salir')
        print('-----------------------')

        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            nombre = input('Ingrese el nombre de la película: ')
            pelicula = Pelicula(nombre)
            CatalogoPeliculas.agregar_pelicula(pelicula)
        elif opcion == '2':
            CatalogoPeliculas.listar_peliculas()
        elif opcion == '3':
            CatalogoPeliculas.eliminar()
        elif opcion == '4':
            print('\nSaliendo del programa.')
        else:
            print('\nOpción no válida.')

if __name__ == '__main__':
    menu()