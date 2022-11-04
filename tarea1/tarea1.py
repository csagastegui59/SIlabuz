import csv

class Libros:
    def __init__(self, archivo = 'libros.csv'):
        self.archivo = archivo
        self.lista = []

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
    with open('tarea1\libros.csv') as file:
        reader = csv.DictReader(file, delimiter = ",")
        for row in reader:
            lista.append(row)
            print(f"\nId: {row['id']}  Libro:{row[' titulo']} ")
            print(f"Género:{row[' genero']} ISBN:{row[' isbn']} Editorial:{row[' editorial']}  Autor:{row[' autor']}")

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