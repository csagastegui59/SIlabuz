import csv

class Libros:
    def __init__(self, archivo = 'tarea1\libros.csv'):
        self.archivo = archivo
        self.lista = []

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
        with open(self.archivo, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter = ",")
            for row in reader:
                self.lista.append(row)
                print(f"\nId: {row['id']}  Libro:{row[' titulo']} ")
                print(f"Género:{row[' genero']} ISBN:{row[' isbn']} Editorial:{row[' editorial']}  Autor:{row[' autor']}")

    def listar(self):
        pass

    def agregar(self):
        pass

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
        pass

    def salir(self):
        pass

Archivo = Libros()
Archivo.menu() 