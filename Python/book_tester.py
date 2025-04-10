from book import Book

books = []
with open("books.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            book = Book(info[0], info[1], info[2])
            print(book)
            books.append(book)

print(books[0].get_title())
print(books[0].get_author())
print(books[0].get_genre())
print(books[0].is_checked_out)

books[0].check_out()
print(books[0])
books[0].return_book()
print(books[0])

        