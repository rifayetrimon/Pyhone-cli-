import csv


def restore_book(filename="library.csv"):
    library = []
    try:
        with open(filename, "r", newline='') as file_pointer:
            all_books = csv.DictReader(file_pointer)
            for detail in all_books:
                book = {
                    "title": detail["title"],
                    "author": detail["author"],
                    "isbn": detail["isbn"],
                    "year": detail["year"],
                    "price": detail["price"],
                    "quantity": detail["quantity"],
                }
                library.append(book)
    except FileNotFoundError:
        print("The file does not exist. Please create a book first.")

    return library


def restore_lent_book(filename="borrower.csv"):
    borrower = []

    try:
        with open(filename, "r", newline='') as file_pointer:
            all_borrower = csv.DictReader(file_pointer)

            for details in all_borrower:
                borrow = {
                    'title': details['title'],
                    'borrow': details['borrow'],
                    'quantity': details['quantity'],
                }
                borrower.append(borrow)

    except FileNotFoundError:
        print("There are no lent item !!!")

    return borrower
