from lent_book import save_details_borrow
from create_book import save_books_to_file


def return_book(borrower, library):
    return_title = input("Enter the book title: ").strip()
    return_borrower = input("Enter the borrower name: ").strip()
    return_quantity = int(input("Enter the quantity you return: "))

    found = False

    for book in borrower:

        if book['title'].strip().lower() == return_title.lower() and book['borrow'].strip().lower() == return_borrower.lower():
            found = True
            if return_quantity <= int(book['quantity']):
                book['quantity'] = str(int(book['quantity']) - return_quantity)
                print("Return book successfully.")
                save_details_borrow(borrower)

                for item in library:
                    if item['title'].strip().lower() == return_title.lower():
                        item['quantity'] = str(int(item['quantity']) + return_quantity)
                        break
                save_books_to_file(library)

                return
            else:
                print("Your return book quantity is more than the lent quantity!")
                return

    if not found:
        print("No matching borrowed book found.")
