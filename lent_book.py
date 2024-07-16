
import csv
from create_book import save_books_to_file


def lent_book(library, borrower):
    search_item = input("Enter a book title or ISBN: ").strip()
    found = False

    for index, book in enumerate(library):
        if search_item.lower() in book['title'].lower() or search_item.lower() in book['isbn'].lower():
            print(
                f"{index + 1}. {book['title']} | {book['author']} | {book['isbn']} | {book['year']} | {book['price']} | {book['quantity']}")
            confirm = input("Do you want to get this book? (yes / no): ").strip().lower()
            if confirm == 'yes':
                borrow = input("Enter your name: ")
                qun_book = int(input("Enter the amount of book you want to lent: "))
                if int(book['quantity']) > qun_book:
                    book['quantity'] = str(int(book['quantity']) - qun_book)
                    if qun_book == 1:
                        print("You get the book successfully !")
                    else:
                        print("You get these books successfully !")
                    save_books_to_file(library)
                    item = {
                        'title': book['title'],
                        'borrow': borrow,
                        'quantity': qun_book
                    }
                    borrower.append(item)
                    save_details_borrow(borrower)
                    return borrower
                else:
                    print("Provided quantity is not available !!")
                found = True
                break
            elif confirm == 'no':
                print("Lets go back to option")
                found = True
                break

    if not found:
        print("No enough book available to lent !")


def save_details_borrow(borrower):
    with open("borrower.csv", "w", newline='') as file_pointer:
        item = ['title', 'borrow', 'quantity']
        writer = csv.DictWriter(file_pointer, fieldnames=item)

        writer.writeheader()
        for book in borrower:
            writer.writerow(book)
