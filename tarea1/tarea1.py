import csv

class Libros:
    def __init__(self, archivo = 'tarea1\libros.csv'):
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
        for row in self.lista:
            print(f"\nId: {row['id']}  Libro:{row[' titulo']} ")
            print(f"Género:{row[' genero']} ISBN:{row[' isbn']} Editorial:{row[' editorial']}  Autor:{row[' autor']}")

    def listar(self):
        pass

    def agregar(self):
        count = len(self.lista)
        titulo = input("Ingrese titulo del libro: ")
        genero = input("Ingrese género del libro: ")
        isbn = int(input("Ingrese ISBN del libro: "))
        editorial = input("Ingrese editorial: ")
        autor = input("Ingrese autor: ")
        dc = {'id': count+1, ' titulo': titulo, ' genero': genero , ' isbn': isbn , ' editorial': editorial, ' autor': autor}
        self.lista.append(dc)
        with open(self.archivo, 'w', encoding="utf-8",newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.fieldnames)
            writer.writeheader()
            writer.writerows(self.lista)

    def eliminar(self):
        pass

    def buscar_isbn_o_titulo(self):
        pass

    def ordenar_titulo(self):
        pass

    def buscar_autor_editorial_o_genero(self):
        pass

    def buscar_numero_de_autores(self):
        pass

    def editar_o_actualizar(self):
        pass

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