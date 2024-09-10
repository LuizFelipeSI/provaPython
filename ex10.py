class Livro(self, library, title, author):

    def add_book(library, title, author):
        self.library = library
        self.title = title
        self.author = author

    def list_books(library):
        if(library):
            print(library)
        else:
            print("não há livros")

    def find_book_by_title(library, title):
        for i in len(library):
            if(library[i].title == title):
                print(library[i])
