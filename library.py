# Book Management System using Dictionary and Set

book_ids = set()      # store book registration numbers
books = {}            # store book details

while True:
    print("\n--- Book Management System ---")
    print("1. Add Book")
    print("2. Delete Book")
    print("3. Total Books")
    print("4. Display All Books")
    print("5. Borrow Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. ADD BOOK
    if choice == 1:
        book_id = int(input("Enter Book ID: "))

        if book_id not in book_ids:
            name = input("Enter Book Name: ")
            author = input("Enter Author Name: ")
            quantity = int(input("Enter Quantity: "))

            book_ids.add(book_id)
            books[book_id] = {
                "name": name,
                "author": author,
                "quantity": quantity
            }
            print("Book added successfully")
        else:
            print("Book ID already exists")

    # 2. DELETE BOOK
    elif choice == 2:
        book_id = int(input("Enter Book ID to delete: "))

        if book_id in book_ids:
            book_ids.remove(book_id)
            del books[book_id]
            print("Book deleted successfully")
        else:
            print("Book not found")

    # 3. TOTAL BOOKS
    elif choice == 3:
        print("Total books:", len(book_ids))

    # 4. DISPLAY ALL BOOKS
    elif choice == 4:
        if not books:
            print("No books available")
        else:
            for bid, details in books.items():
                print("ID:", bid, "Details:", details)

    # 5. BORROW BOOK
    elif choice == 5:
        book_id = int(input("Enter Book ID to borrow: "))

        if book_id in books:
            if books[book_id]["quantity"] > 0:
                books[book_id]["quantity"] -= 1
                print("Book borrowed successfully")
            else:
                print("Book out of stock")
        else:
            print("Book not found")

    # 6. EXIT
    elif choice == 6:
        print("Exiting Book Management System")
        break

    else:
        print("Invalid choice")