import requests

class BookService:
    # BASE_URL = "http://127.0.0.1:8000"
    BASE_URL = "http://fastapi-cli-book-task-production.up.railway.app"
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
        
        if isinstance(data, list):
            if len(data) > 0:
                data = data[0]
            else:
                print("The server returned empty list, make sure u've saved the data in the backend.")
                data = {}
                
        return {
            "title": "Book Created",
            "items": {
                "ID": data.get("id", "N/A"),         
                "Title": data.get("title", "N/A"),
                "Author": data.get("author", "N/A"),
                "Status": "Active" if data.get("is_active", True) else "Inactive"
            }
        }
    ###
    # def create_book(self, title, author):
    #     response = requests.post(f"{self.BASE_URL}/books", json={"title": title, "author": author}, timeout=10)
    #     response.raise_for_status()
    #     data = response.json()
        
    #     if isinstance(data, list):
    #         if len(data) > 0:
    #             data = data[0]
    #         else:
    #             raise Exception("Server returned an empty list")
                
    #     return {
    #         "title": "Book Created",
    #         "items": {
    #             "ID": data.get("id"),         
    #             "Title": data.get("title"),
    #             "Author": data.get("author"),
    #             "Status": "Active" if data.get("is_active", True) else "Inactive"
    #         }
    #     }
    ### 
    # def create_book(self, title, author):
    #     response = requests.post(f"{self.BASE_URL}/books", json={"title": title, "author": author}, timeout=10)
    #     response.raise_for_status()
    #     data = response.json()
    #     if isinstance(data, list) and len(data) > 0:
    #         data = data[0]
            
    #     return {
    #         "title": "Book Created",
    #         "items": {
    #             "ID": data["id"],
    #             "Title": data["title"],
    #             "Author": data["author"],
    #             "Status": "Active"
    #         }
    #     }

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