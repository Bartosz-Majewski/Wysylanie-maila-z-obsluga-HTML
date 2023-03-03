import sqlite3


def create_connection(database_name):
    with sqlite3.connect(database_name) as connection:
        cursor = connection.cursor()
        return cursor


def get_person(cursor, today_date):
    """Downloading information from database about readers"""
    cursor.execute('SELECT * FROM books WHERE return_at<=?', (today_date,))
    data = []
    for book in cursor.fetchall():
        book_id, client_name, client_surname, email, book_title, rental_date, return_at = book
        data.append({
            'Client name': client_name,
            'E-mail': email,
            'Book title': book_title,
            'Return date': return_at
        })
    return data
