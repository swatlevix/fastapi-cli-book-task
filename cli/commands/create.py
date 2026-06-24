from services.book_service import BookService
from utils.formatter import Formatter

class CreateCommand:
    def execute(self, args):
        if len(args) < 2:
            print("Usage: create <title> <author>")
            return
        title = args[0]
        author = args[1]
        Formatter.display(BookService().create_book(title, author))