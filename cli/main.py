import sys
from commands.books import BooksCommand
from commands.book import BookCommand
from commands.create import CreateCommand
from commands.delete import DeleteCommand
from commands.update import UpdateCommand

COMMANDS = {
    "books": BooksCommand(),
    "book": BookCommand(),
    "create": CreateCommand(),
    "delete": DeleteCommand(),
    "update": UpdateCommand(), 
}


def main():
    if len(sys.argv) < 2:
        print("Commands Available: ")
        print("  books [author]        List all books (or filter by author)")
        print("  book <id>             View specific book details")
        print("  create <title> <auth> Add a new book")
        print("  delete <id>           Remove a book from library")
        print("  update <id> <title> <auth> Update an existing book details")
        return

    command = sys.argv[1]
    args = sys.argv[2:]

    handler = COMMANDS.get(command)
    if not handler:
        print(f"Unknown command: {command}")
        return

    handler.execute(args)

if __name__ == "__main__":
    main()