
class Client:
    def _init_(self, id, full_name, age, id_no, phone_number):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number

class Librarian:
    def _init_(self, id, full_name, age, id_no, employment_type):
        self.id = id
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.employment_type = employment_type

class Book:
    def _init_(self, id, title, description, author, status):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.status = status

class BorrowingOrder:
    def _init_(self, id, date, client_id, book_id, status):
        self.id = id
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status

class MainFile:
    def _init_(self):
        self.clients = []
        self.librarians = []
        self.books = []
        self.borrowed_orders = []

    def create_client(self, id, full_name, age, id_no, phone_number):
        new_client = Client(id, full_name, age, id_no, phone_number)
        self.clients.append(new_client)
        print("Client added successfully")

    def create_librarian(self, id, full_name, age, id_no, employment_type):
        new_librarian = Librarian(id, full_name, age, id_no, employment_type)
        self.librarians.append(new_librarian)
        print("Librarian added successfully")

    def create_book(self, id, title, description, author, status):
        new_book = Book(id, title, description, author, status)
        self.books.append(new_book)
        print("Book added successfully")

    def borrow_book(self, librarian_id_no, client_id_no, book_id):
        librarian = next((l for l in self.librarians if l.id_no == librarian_id_no), None)
        if not librarian:
            print("Invalid librarian id")
            return
        client = next((c for c in self.clients if c.id_no == client_id_no), None)
        if not client:
            print("Invalid client id")
            return
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            print("Invalid book id")
            return
        if book.status != "Available":
            print("Book is not available for borrowing")
            return
        order_id = len(self.borrowed_orders) + 1
        new_order = BorrowingOrder(order_id,client.id, book.id, "Active")
        self.borrowed_orders.append(new_order)
        book.status = "Unavailable"
        print("Book borrowed successfully. Order ID: ", order_id)

    def show_all_books(self):
        for book in self.books:
            print("ID: ", book.id)
            print("Title: ", book.title)
            print("Author: ", book.author)
            print("Status: ", book.status)

    def show_all_orders(self):
        for order in self.borrowed_orders:
            print("Order ID: ", order.id)
            print("Date: ", order.date)
            print("Client ID: ", order.client_id)
            print("Book ID: ", order.book_id)
            print("Status: ", order.status)

    def show_all_books(self):
        pass


mainfile = MainFile()
while True:
    user_input = ""
    while user_input != "3":
        print("1- Enter as a client.\n2- Enter as a librarian.\n3- Exit. ")
        user_input = input()
        if user_input == "1":
            id = int(input("Enter your id:"))
            full_name = input("Enter your full name: ")
            age = int(input("Enter your age: "))
            id_no = input("Enter your idNo: ")
            phone_number = input("Enter your phone number: ")
            mainfile.create_client(id, full_name, age, id_no, phone_number)
        elif user_input == "2":
            inp = input("1- Enter librarian.\n2- Book.\n3- order.")
            if inp == "1":
                id = int(input("Enter your id:"))
                full_name = input("Enter your full name: ")
                age = int(input("Enter your age: "))
                id_no = input("Enter your idNo: ")
                employment_type = input("Enter your employment type: ")
                mainfile.create_librarian(id, full_name, age, id_no, employment_type)
            if inp == "2":
                input1 = ""
                while input1 != "3":
                    print("1- Create 3 books\n2- Show all books\n3- Exit")
                    input1 = input()
                    if input1 == "1":
                        for i in range(3):
                            book_id = int(input("Enter book id: "))
                            title = input("Enter book title: ")
                            description = input("Enter book description: ")
                            author = input("Enter book author: ")
                            status = input("Enter book status (Available/Borrowed): ")
                            mainfile.create_book(book_id, title, description, author, status)
                    elif input1 == "2":
                        mainfile.show_all_books()
                    elif input1 == "3":
                        break
                    else:
                        print("Invalid input, please try again")

            if inp == "3":
                while True:
                    print("1- borrow book\n2- show show all orders\n3- Exit")
                    inp = input()
                    if inp == "1":
                        print("Enter librarian idNo: ")
                        librarian_id_no = input()
                        print("Enter client idNo: ")
                        client_id_no = input()
                        print("Enter book id: ")
                        book_id = int(input())
                        mainfile.borrow_book(librarian_id_no, client_id_no, book_id)
                    elif inp == "2":
                        mainfile.show_all_orders()
                    elif inp == "3":
                        break
                    else:
                        print("Invalid input, please try again")
    if user_input == "Exit":
        pass