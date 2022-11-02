import csv

class Libro:
    def _init_(self, id:int=None, titulo:str=None, genero:str=None, isbn:int=None, editorial:str=None, autor:str=None):
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def open_csv(self):
        with open('libros.csv', 'r', encoding='utf-8') as f:
            book = csv.reader(f)
            books = [row for row in book] 
            return books

    # Opción 2: Listar libros
    def show_books(books):
        listBooks = books.open_csv()
        libros = [row[1] for row in listBooks]
        print(libros)

    # Opción 5: Buscar libro por ISBN o por titulo. Se debe sugerir las opciones y listar los resultados
    def search_isbn_titulo(books):
        listBooks = books.open_csv()
        print(f"Se puede realizar la busqueda por ISBN o por el título de los libros")
        selection = input("Ingrese el ISBN o título a buscar: ")
        for i in listBooks:
            if i[1] == selection or i[3] == selection:
                print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")
    
    # Opción 6: Ordenar libros por titulo 
    def sort_by_books(books):
        listBooks = books.open_csv()
        libros = [row[1] for row in listBooks]
        libros.sort()
        print(libros)
    
    # Opción 7: Buscar libros por autor, editorial o genero. Se deben sugerir las opciones y listar los resultados
    def search_autor_editorial_genero(books):
        listBooks = books.open_csv()
        print(f"Pueden realizar una busqueda por autor, editorial o género de los libros")
        selection = input("Ingrese el autor, editorial o genero a buscar: ").lower()
        for i in listBooks:
            if i[5].lower() == selection or i[4].lower() == selection or i[2].lower() == selection:
                print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")


q = Libro()
#q.open_csv()
#q.show_books()
#q.search_isbn_titulo()
#q.sort_by_books()
q.search_autor_editorial_genero()