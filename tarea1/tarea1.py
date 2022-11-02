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

    def show_books(books):
        listBooks = books.open_csv()
        libros = [row[1] for row in listBooks]
        print(libros)

    def search_isbn_titulo(books):
        listBooks = books.open_csv()
        print(f"Se puede realizar la busqueda por ISBN o por el título de los libros")
        selection = input("Ingrese el ISBN o título a buscar: ")
        for i in listBooks:
            if str(i[1]) == selection:
                print(f"{i[0]} - {i[1]} - {i[2]} - {i[3]} - {i[4]} - {i[5]}")

q = Libro()
q.open_csv()
q.show_books()
q.search_isbn_titulo()