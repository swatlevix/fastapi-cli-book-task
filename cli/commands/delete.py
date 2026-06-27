from services.book_service import BookService
from utils.formatter import Formatter

class DeleteCommand:
    def execute(self, args):
        if not args:
            print("Usage: python main.py delete <id>")
            return
        try:
            BookService().delete_book(int(args[0]))
            print(f"Book with ID {args[0]} has been successfully deleted.")
        except Exception as e:
            print("Could not delete book. ID might be invalid.")