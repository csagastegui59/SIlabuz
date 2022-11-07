import pandas as pd
import csv
import time


class Libros:
    def __init__(self, archivo="Libros.csv"):
        self.archivo = archivo
        self.lista = []
        with open(self.archivo, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.lista.append(row)
        self.fieldnames = ['id', 'titulo', 'genero', 'isbn', 'editorial', 'autor']

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
            seleccion = int(input("Elija una opción: "))
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
        for row in self.lista:
            print(f"\nId: {row['id']}  Libro: {row['titulo']} ")
            print(f"Género: {row['genero']} ISBN: {row['isbn']} Editorial: {row['editorial']}  Autor: {row['autor']}")

    def listar(self):
        print(f"\n << OPCIÓN 2: LISTAR LIBROS >> \n")
        time.sleep(2)
        libros = pd.read_csv(self.archivo, encoding="utf-8")
        print(libros)
        time.sleep(3)
        print("\n<< FIN DEL PROCESO >>")

    def agregar(self):
        count = len(self.lista)
        titulo = input("Ingrese titulo del libro: ")
        genero = input("Ingrese género del libro: ")
        isbn = input("Ingrese ISBN del libro: ")
        editorial = input("Ingrese editorial: ")
        autor = input("Ingrese autor: ")
        dc = {'id': count+1, 'titulo': titulo, 'genero': genero , 'isbn': isbn , 'editorial': editorial, 'autor': autor}
        self.lista.append(dc)
        with open(self.archivo, 'w', encoding="utf-8",newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.lista)

    def eliminar(self):
      print("\n<< OPCIÓN 4: ELIMINAR LIBRO >>\n")
      option =input("\nIngrese el id del libro que desea eliminar: ")
      for book in self.lista:
        if (book['id'] == option):
          self.lista.remove(book)

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
      print("\n<< OPCIÓN 8: BUSCAR POR NUMERO DE AUTORES >>\n")
      option =int(input("\nIngrese el numero de autores: "))
      lista1 = []
      result = []
      with open(self.archivo, 'r', encoding='utf-8') as file:
        reader1 = csv.DictReader(file, restkey='autor',fieldnames = ['id', 'titulo', 'genero', 'isbn', 'editorial'])
        for row in reader1:
          lista1.append(row)
        lista1.pop(0)
      for book in lista1:
        if (len(book['autor']) == option):
          result.append(book)
      if len(result) == 0:
        print('No se encontraron libros con ese numero de autores')
      else:
        for i in result:
          print(f"ID: {i['id']} | TÍTULO: {i['titulo']} | GÉNERO: {i['genero']} | ISBN: {i['isbn']} | EDITORIAL: {i['editorial']} | AUTOR: {i['autor']}")        

    def editar_o_actualizar(self):
      print("\n<< OPCIÓN 9: ACTUALIZAR LIBRO >>\n")
      option =input("\nIngrese el id del libro que desea actualizar: ")
      for book in self.lista:
        if (book['id'] == option):
          titulo = input("Ingrese titulo del libro: ")
          genero = input("Ingrese género del libro: ")
          isbn = input("Ingrese ISBN del libro: ")
          editorial = input("Ingrese editorial: ")
          autor = input("Ingrese autor: ")

          book['titulo'] = titulo,
          book['genero'] = genero,
          book['isbn'] = isbn,
          book['editorial'] = editorial,
          book['autor'] = autor,


    def guardar(self):
        #Guradar libros en archivo
        my_path = 'nuevo_libro.csv'
        with open(my_path, 'w', encoding="utf-8",newline='') as file:
            writer = csv.DictWriter(file,fieldnames=self.fieldnames,delimiter='|')
            writer.writeheader()
            writer.writerows(self.lista)
        file.close()
        print("Se han guardado los datos en un nuevo archivo.")

    def salir(self):
        pass

Archivo = Libros()
Archivo.menu() 
