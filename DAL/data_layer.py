from DAL.database import db

TABLE_NAME = "books"

def get_books():
    return db.table(TABLE_NAME).select("*").execute().data

def get_book(book_id):
    result = db.table(TABLE_NAME).select("*").eq("id", book_id).execute().data
    return result[0] if result else None

def create_book(book):
    result = db.table(TABLE_NAME).insert(book).execute().data
    return result[0] if isinstance(result, list) and len(result) > 0 else result

def update_book(book_id, updated_data):
    result = db.table(TABLE_NAME).update(updated_data).eq("id", book_id).execute().data
    return result[0] if isinstance(result, list) and len(result) > 0 else result

def delete_book(book_id):
    db.table(TABLE_NAME).delete().eq("id", book_id).execute()

