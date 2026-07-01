# from fastapi import FastAPI, HTTPException, status, Query
# from typing import List, Optional
# from .database import BOOKS_DB
# from .schemas import BookCreate, BookResponse

# app = FastAPI(title="Book Management System API", version="1.0.0")

# @app.get("/books", response_model=List[BookResponse])
# def get_books(author: Optional[str] = Query(None, min_length=1)):
#     books_list = list(BOOKS_DB.values())
#     if author:
#         books_list = [b for b in books_list if author.lower() in b["author"].lower()]
#     return books_list

# @app.get("/books/{book_id}", response_model=BookResponse)
# def get_book(book_id: int):
#     book = BOOKS_DB.get(book_id)
#     if not book:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#     return book

# @app.post("/books", response_model=BookResponse, status_code=201)
# def create_book(payload: BookCreate):
#     next_id = max(BOOKS_DB.keys(), default=0) + 1
#     new_book = {
#         "id": next_id,
#         "title": payload.title,
#         "author": payload.author,
#         "is_active": True
#     }
#     BOOKS_DB[next_id] = new_book
#     return new_book

# @app.put("/books/{book_id}", response_model=BookResponse)
# def update_book(book_id: int, payload: BookCreate):
#     if book_id not in BOOKS_DB:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#     BOOKS_DB[book_id].update({"title": payload.title    , "author": payload.author})
#     return BOOKS_DB[book_id]

# @app.put("/books/{book_id}/toggle-status", response_model=BookResponse)
# def toggle_book_status(book_id: int):
#     if book_id not in BOOKS_DB:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#     BOOKS_DB[book_id]["is_active"] = not BOOKS_DB[book_id]["is_active"]
#     return BOOKS_DB[book_id]

# @app.delete("/books/{book_id}", status_code=204)
# def delete_book(book_id: int):
#     if book_id not in BOOKS_DB:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
#     del BOOKS_DB[book_id]
#     return

######

###

from typing import List, Optional
from fastapi import FastAPI, HTTPException, status, Query

from .schemas import BookCreate, BookResponse

from DAL.data_layer import (
    create_book,
    delete_book,
    get_book,
    get_books,
    update_book,
)

app = FastAPI(title="Book Management System API", version="1.0.0")


@app.get("/books", response_model=List[BookResponse], status_code=status.HTTP_200_OK)
def get_books_endpoint(author: Optional[str] = Query(None, min_length=1)):
    books_list = get_books()
    if author:
        books_list = [b for b in books_list if author.lower() in b["author"].lower()]
    return books_list


@app.get("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def get_book_endpoint(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    return book


@app.post("/books", response_model=BookResponse, status_code=status.HTTP_201_CREATED)
def create_book_endpoint(payload: BookCreate):
    book_data = payload.model_dump() # بتحول البيانات dict
    book_data["is_active"] = True
    new_book = create_book(book_data)
    return new_book


@app.put("/books/{book_id}", response_model=BookResponse, status_code=status.HTTP_200_OK)
def update_book_endpoint(book_id: int, payload: BookCreate):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    updated_book = update_book(book_id, payload.model_dump())
    return updated_book


@app.put("/books/{book_id}/toggle-status", response_model=BookResponse, status_code=status.HTTP_200_OK)
def toggle_book_status_endpoint(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    new_status = not book["is_active"]
    updated_book = update_book(book_id, {"is_active": new_status})
    return updated_book


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book_endpoint(book_id: int):
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
    
    delete_book(book_id)
    return None