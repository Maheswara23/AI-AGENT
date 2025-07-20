import sqlite3
import os

def get_connection():
    """
    Returns a connection to the database located at the project root (next to main.py).
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))  # engine/
    db_path = os.path.normpath(os.path.join(base_dir, "..", "database.db"))  # ../database.db

    # Debug print to confirm it's the correct path
    print(f"📂 Connecting to DB at: {db_path}")

    return sqlite3.connect(db_path)
