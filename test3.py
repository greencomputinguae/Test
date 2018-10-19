from test1 import databaseconnection
from typing import List, Dict
#BOOK=Dict(str, Union(str, int))
def create_table()->None:
    with databaseconnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS books(name text PRIMARY KEY, author text, read integer)')


def add_book(name: str,author: str)->None:
    with databaseconnection('data.db') as connection:

        cursor=connection.cursor()
        cursor.execute("INSERT INTO books VALUES (?,?,1)", (name,author))


def delete_book(name:str)->None:
    with databaseconnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('DELETE FROM books WHERE name=?', (name,))

def show_book():
    with databaseconnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('SELECT * FROM books')
        books=[ {'name':row[0], 'author':row[1], 'read':row[2]} for row in cursor.fetchall()]
        return books

def change_book(name:str)->None:
    with databaseconnection('data.db') as connection:
        cursor=connection.cursor()
        cursor.execute('UPDATE books SET read=1 WHERE name=?' (name,))
