from services.book_service import BookService
from utils.formatter import Formatter

class BookCommand:
    def execute(self, args):
        if not args:
            print("Usage: book <id>")
            return
        try:
            book_id = int(args[0])
        except ValueError:
            print("Error: Book ID must be a number.")
            return
        Formatter.display(BookService().get_book(book_id))