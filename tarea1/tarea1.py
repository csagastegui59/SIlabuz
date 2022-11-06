import csv
import pandas as pd

class Libros:
    def __init__(self, archivo):
        self.archivo = archivo
        self.lista = []
        with open(self.archivo, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.lista.append(row)
        self.fieldnames = ['id', ' titulo', ' genero', ' isbn', ' editorial', ' autor']

    def menu(self):
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
                self.leer_archivo()
            if seleccion == 2:
                self.listar()
            if seleccion == 3: 
                self.agregar()
            if seleccion == 4:
                self.eliminar()
            if seleccion == 5:
                self.buscar_isbn_o_titulo()
            if seleccion == 6:
                self.ordenar_titulo()
            if seleccion == 7:
                self.buscar_autor_editorial_o_genero()
            if seleccion == 8:
                self.buscar_numero_de_autores()
            if seleccion == 9:
                self.editar_o_actualizar()
            if seleccion == 10:
                self.guardar()
            if seleccion == 11:
                self.salir()
        
    def leer_archivo(self):
        pass

    def listar(self):
        libros = pd.read_csv(self.archivo, encoding="utf-8")
        print(libros)
        pass

    def agregar(self):
        pass

    def eliminar(self):
        pass

    def buscar_isbn_o_titulo(self):
        listBooks = self.lista
        print(f"Se puede realizar la busqueda por ISBN o por el título de los libros")
        selection = input("Ingrese el ISBN o título a buscar: ")
        for i in listBooks:
            if i['titulo'].lower() == selection.lower() or i['isbn'] == selection:
                print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")

    def ordenar_titulo(self):
        listBooks = self.lista
        libros = [row['titulo'] for row in listBooks]
        libros.sort()
        for i in range(len(libros)):
            print(f"{i+1}: {libros[i]}")

    def buscar_autor_editorial_o_genero(self):
        listBooks = self.lista
        print(f"Pueden realizar una busqueda por autor, editorial o género de los libros")
        selection = input("Ingrese el autor, editorial o genero a buscar: ").lower()
        for i in listBooks:
            if i['autor'].lower() == selection.lower() or i['editorial'].lower() == selection.lower() or i['genero'].lower() == selection.lower():
                print(f"ID: {i['id']} | TITULO: {i['titulo']} | GENERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")

    def buscar_numero_de_autores(self):
        pass

    def editar_o_actualizar(self):
        pass

    def guardar(self):
        pass

    def salir(self):
        pass


path_archivo = 'tarea1\libros.csv'
archivo = Libros(path_archivo)
archivo.menu() 