from services.book_service import BookService
from utils.formatter import Formatter

class DeleteCommand:
    def execute(self, args):
        if not args:
            print("Usage: python main.py delete <id>")
            return
        try:
            BookService().delete_course(int(args[0]))  # اتبعنا تسميات الدكتور في الحذف
            Formatter.display_success(f"Book with ID {args[0]} has been successfully deleted.")
        except Exception as e:
            Formatter.display_error("Could not delete book. ID might be invalid.")