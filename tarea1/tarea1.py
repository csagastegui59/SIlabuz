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
        with open("libros.csv", "r", encoding='utf-8') as f:
            book = csv.reader(f)
            books = [row for row in book] 
            print(books)
        return books

    def show_books(self, books):
        print(books)
        libros = [row[1] for row in self.books]
        print(libros)


q = Libro()
q.open_csv()
q.show_books()