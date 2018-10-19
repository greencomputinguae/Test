from test3 import add_book, create_table, change_book, delete_book, show_book
import sqlite3




def menu():
    string="""

               -a add new book
               -l show list of books
               -d delete the book based on name
               -r change statudde to read
               -q for quite

               please choose a letter:

    """
    inp=input(string)
    while inp!='q':
        create_table()
        if inp=='a':
            name=input("Please enter the name of the book: ")
            author = input("Please enter the author of the book: ")
            add_book(name,author)
        if inp == 'd':
            name = input("Please enter the name of the book: ")
            delete_book(name)
        if inp == 'l':
            books=show_book()
            for i in books:
                print(f"{i['name']} is the name of the book, {i['author']}")
        if inp == 'r':
            name = input("Please enter the name of the book: ")
            change_book(name)
        inp = input(string)

menu()