import csv

def menu():
    seleccion = 0
    while seleccion != 11:
        print('''
        Opción 1: Leer archivo.
        Opción 2: Listar libros.
        Opción 3: Agregar libro.
        Opción 4: Eliminar libro.
        Opción 5: Buscar libro por ISBN o por título. 
        Opción 6: Ordenar libros por título.
        Opción 7: Buscar libros por autor, editorial o género. 
        Opción 8: Buscar libros por número de autores.
        Opción 9: Editar o actualizar datos de un libro.
        Opción 10: Guardar libros en archivo.
        Opción 11: Salir.
        ''')
        seleccion = int(input("Eliga una opción: "))