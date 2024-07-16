import csv


def create_book(library):
    title = input("Enter the book title: ").strip()
    author = input("Enter the author name (use comma for separate): ").strip()
    isbn = input("Enter the book isbn: ").strip()
    year = int(input("Enter the publish year: ").strip())
    price = float(input("Enter the book price: ").strip())
    quantity = int(input("Book Quantity: ").strip())

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": year,
        "price": price,
        "quantity": quantity
    }

    library.append(book)
    save_books_to_file(library)
    print("Book created successful!")
    return library


def save_books_to_file(library):
    with open("library.csv", "w", newline='') as file_pointer:
        item = ['title', 'author', 'isbn', 'year', 'price', 'quantity']
        writer = csv.DictWriter(file_pointer, fieldnames=item)

        writer.writeheader()
        for book in library:
            writer.writerow(book)






