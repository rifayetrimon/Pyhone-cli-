from create_book import save_books_to_file



def remove_book(library):
    search_result = input("Enter a book title or ISBN: ").strip()
    found = False

    for index, book in enumerate(library):
        if search_result.lower() in book['title'].lower() or search_result.lower() in library['isbn'].lower():
            print(
                f"{index + 1}. {book['title']} | {book['author']} | {book['isbn']} | {book['year']} | {book['price']} | {book['quantity']}")
            confirm = input("Do you want to remove this book? (yes / no): ").strip().lower()
            if confirm == 'yes':
                library.pop(index)
                print(f"{book['title']} is successfully deleted")
                save_books_to_file(library)
                found = True
                break
            elif confirm == 'no':
                print("Lets go back to option ")
                found = True
                break

    if not found:
        print("There is no book with this title or ISBN number!")
