# BOOKS_DB = {
#     1: {"id": 1, "title": "Ketab 1", "author": "Ahmed", "is_active": True},
#     2: {"id": 2, "title": "Ketab tany", "author": "Kateb elketab eltany", "is_active": False}
# }
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

db = create_client(SUPABASE_URL, SUPABASE_KEY)