


def view_lent(borrower):
    if not borrower:
        print("No book have been lent")
        return
    print("Title", "Borrower", "Quantity", sep=" | ")
    for book in borrower:
        print(book['title'], book['borrow'], book['quantity'], sep=" - ")




