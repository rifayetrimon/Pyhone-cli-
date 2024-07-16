import csv


def view_book(libray):

    print("Title", "Author", "ISBN", "Year", "Price", "Quantity")
    for book in libray:
        print(book['title'], book['author'], book['isbn'], book['year'], book['price'], book['quantity'],
              sep="  |  ")






