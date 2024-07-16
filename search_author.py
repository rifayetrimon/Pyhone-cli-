
def search_by_author(library):
    search_item = input("Enter author name to search book: ").strip()
    found = []

    for book in library:
        if search_item.lower() in book['author'].lower():
            found.append(book)

    if found:
        if len(found) == 1:
            print(f"{found[0]['author']} writes this book")
        else:
            print(f"{found[0]['author']} writes these book")

        for book in found:
            print(book['title'], book['author'], book['isbn'], book['year'], book['price'], book['quantity'],
                  sep="  | ")
    else:
        print(f"Here is not book by this author {search_item.upper()}")










