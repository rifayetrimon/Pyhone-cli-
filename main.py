import create_book
import lent_book
import return_book
import search_author
import search_book
import view_book
import remove_book
import restore
import view_lent

library = restore.restore_book()

borrower = restore.restore_lent_book()

# print(type(borrower))

menu_opt = """
Select a option.....
1. Create a book
2. See Library
3. Search Book
4. Remove Book
5. Search by author name
6. Lent Book
7. View Lent Book
8. Return Book
0. Exit
"""



while True:
    print(menu_opt)
    chose = int(input("Choose a option : ").strip())

    if chose == 1:
        library = create_book.create_book(library)
    elif chose == 2:
        view_book.view_book(library)
    elif chose == 3:
        search_book.search_book(library)
    elif chose == 4:
        remove_book.remove_book(library)
    elif chose == 5:
        search_author.search_by_author(library)
    elif chose == 6:
        lent_book.lent_book(library, borrower)
    elif chose == 7:
        view_lent.view_lent(borrower)
    elif chose == 8:
        return_book.return_book(borrower, library)
    elif chose == 0:
        print("Have a nice day !")
        break
    else:
        print("Invalid option !")
    continue






