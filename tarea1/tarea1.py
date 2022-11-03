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
        if seleccion == 1:
            leer_archivo()
        if seleccion == 2:
            listar()
        if seleccion == 3: 
            agregar()
        if seleccion == 4:
            eliminar()
        if seleccion == 5:
            buscar_isbn_o_titulo()
        if seleccion == 6:
            ordenar_titulo()
        if seleccion == 7:
            buscar_autor_editorial_o_genero()
        if seleccion == 8:
            buscar_numero_de_autores()
        if seleccion == 9:
            editar_o_actualizar()
        if seleccion == 10:
            guardar()
        if seleccion == 11:
            salir()
    
def leer_archivo():
    pass

def listar():
    pass

def agregar():
    pass

def eliminar():
    pass

def buscar_isbn_o_titulo():
    pass

def ordenar_titulo():
    pass

def buscar_autor_editorial_o_genero():
    pass

def buscar_numero_de_autores():
    pass

def editar_o_actualizar():
    pass

def guardar():
    pass

def salir():
    pass

menu() 