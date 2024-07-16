

def search_book(library):
    search_item = input("Enter a book title or ISBN: ").strip()
    found = False

    for book in library:
        if search_item.lower() in book['title'].lower() or search_item.lower() in book['isbn'].lower():
            print("Found the book successfully")
            print(book['title'], book['author'], book['isbn'], book['year'], book['price'], book['quantity'],
                  sep="  | ")
            found = True
    if not found:
        print("There are no book with these title or Isbn number !!!")


