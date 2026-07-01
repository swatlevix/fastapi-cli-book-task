from services.book_service import BookService
from utils.formatter import Formatter

class UpdateCommand:
    def execute(self, args):
        if len(args) < 3:
            print("Usage: update <id> <new_title> <new_author>")
            return
        
        try:
            book_id = int(args[0])
        except ValueError:
            print("Error: Book ID must be a number.")
            return
            
        new_title = args[1]
        new_author = args[2]
        
        try:
            result = BookService().update_book(book_id, new_title, new_author)
            Formatter.display(result)
        except Exception as e:
            print(f"Could not update book. Error: {e}")