from services.book_service import BookService
from utils.formatter import Formatter

class BooksCommand:
    def execute(self, args):
        author_filter = args[0] if args else None
        Formatter.display(BookService().list_books(author_filter))