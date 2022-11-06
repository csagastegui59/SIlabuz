import pandas as pd
import csv
import time


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
            Bienvenidos al programa sobre consultas de libros y sus caracteristicas
            LIBRO-CONSULTAS v1.0
            Elija una de las siguientes opciones:

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
        print(f"\n << OPCIÓN 2: LISTAR LIBROS >> \n")
        time.sleep(2)
        libros = pd.read_csv(self.archivo, encoding="utf-8")
        print(libros)
        time.sleep(3)
        print("\n<< FIN DEL PROCESO >>")

    def agregar(self):
        pass

    def eliminar(self):
        pass

    def buscar_isbn_o_titulo(self):
        print("\n<< OPCIÓN 5: BUSCAR LIBRO POR ISBN O POR TÍTULO >>\n")
        time.sleep(1)
        listBooks = self.lista                
        opcion = 0
        while opcion != "3" or opcion != ' ':
            print("Puede realizar la busqueda por ISBN o por el título de los libros \n")
            print("1.- Busqueda por ISBN")
            print("2.- Busqueda por Título")
            print("3.- Finalizar")
            opcion = input("\n Escoja la opción: ")
            if opcion == "1":
                selection = input("\n Ingrese el ISBN que quiere buscar: ")
                print("\n")
                time.sleep(2)
                for i in listBooks:
                    if i['isbn'] == selection:
                        print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")        
                time.sleep(3)
                print("\n")

            elif opcion == "2":
                selection = input("\n Ingrese el título que quiere buscar: ")
                print("\n")
                time.sleep(2)
                for i in listBooks:
                    if i['titulo'].lower() == selection.lower():
                        print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")
                time.sleep(3)
                print("\n")

            elif opcion == "3":
                time.sleep(1)
                print("\n<< FIN DE LAS CONSULTAS >>")
                time.sleep(1)
                break

    def ordenar_titulo(self):
        print(f"\n << OPCIÓN 6: ORDENAR LIBROS POR TÍTULO >> \n")
        time.sleep(2)
        listBooks = self.lista
        libros = [row['titulo'] for row in listBooks]
        libros.sort()
        for i in range(len(libros)):
            print(f"{i+1}: {libros[i]}")
        time.sleep(3)
        print("\n<< FIN DEL PROCESO >>")

    def buscar_autor_editorial_o_genero(self):
        print("\n<< OPCIÓN 7: BUSCAR LIBROS POR AUTOR, EDITORIAL O GENERO >>\n")
        time.sleep(1)
        listBooks = self.lista                
        opcion = 0
        while opcion != "4" or opcion !=' ':
            print("Puede realizar la busqueda por autor, editorial o género de los libros \n")
            print("1.- Búsqueda por autor")
            print("2.- Búsqueda por editorial")
            print("3.- Búsqueda por género")
            print("4.- Finalizar")
            opcion = input("\n Escoja la opción: ")
            if opcion == "1":
                selection = input("\n Ingrese el autor que quiere buscar: ")
                print("\n")
                time.sleep(2)
                for i in listBooks:
                    if i['autor'].lower() == selection.lower():
                        print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")        
                time.sleep(3)
                print("\n")

            elif opcion == "2":
                selection = input("\n Ingrese la editorial que quiere buscar: ")
                print("\n")
                time.sleep(2)
                for i in listBooks:
                    if i['editorial'].lower() == selection.lower():
                        print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")
                time.sleep(3)
                print("\n")
            
            elif opcion =="3":
                selection = input("\n Ingrese el género que quiere buscar: ")
                print("\n")
                time.sleep(2)
                for i in listBooks:
                    if i['genero'].lower() == selection.lower():
                        print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")
                time.sleep(3)
                print("\n")

            elif opcion == "4":
                time.sleep(1)
                print("\n<< FIN DE LAS CONSULTAS >>")
                time.sleep(1)
                break
            
    def buscar_numero_de_autores(self):
        pass

    def editar_o_actualizar(self):
        pass

    def guardar(self):
        pass

    def salir(self):
        pass


path_archivo = 'libros.csv'
archivo = Libros(path_archivo)
archivo.menu() 