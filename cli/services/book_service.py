import requests

class BookService:
    BASE_URL = "http://127.0.0.1:8000"

    def list_books(self, author=None):
        params = {"author": author} if author else None
        response = requests.get(f"{self.BASE_URL}/books", params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": "All Books" if not author else f"Books by {author}",
            "items": {str(b["id"]): f"{b['title']} (By: {b['author']})" for b in data}
        }

    def get_book(self, book_id):
        response = requests.get(f"{self.BASE_URL}/books/{book_id}", timeout=10)
        response.raise_for_status()
        data = response.json()
        status_str = "Active" if data["is_active"] else "Inactive"
        return {
            "title": "Book Details",
            "items": {
                "ID": data["id"],
                "Title": data["title"],
                "Author": data["author"],
                "Status": status_str
            }
        }

    def create_book(self, title, author):
        response = requests.post(f"{self.BASE_URL}/books", json={"title": title, "author": author}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": "Book Created",
            "items": {
                "ID": data["id"],
                "Title": data["title"],
                "Author": data["author"],
                "Status": "Active"
            }
        }

    def update_book(self, book_id, title, author):
        response = requests.put(f"{self.BASE_URL}/books/{book_id}", json={"title": title, "author": author}, timeout=10)
        response.raise_for_status()
        data = response.json()
        return {
            "title": "Book Updated",
            "items": {
                "ID": data["id"],
                "Title": data["title"],
                "Author": data["author"]
            }
        }

    def toggle_status(self, book_id):
        response = requests.put(f"{self.BASE_URL}/books/{book_id}/toggle-status", json={}, timeout=10)
        response.raise_for_status()
        data = response.json()
        status_str = "Active" if data["is_active"] else "Inactive"
        return {
            "title": "Status Changed",
            "items": {
                "Title": data["title"],
                "New Status": status_str
            }
        }

    def delete_book(self, book_id):
        response = requests.delete(f"{self.BASE_URL}/books/{book_id}", timeout=10)
        response.raise_for_status()
        return {
            "title": "Book Deleted",
            "items": {"Message": f"Book {book_id} has been removed successfully."}
        }