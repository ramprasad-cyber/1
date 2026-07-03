import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "gym.db"
SQL_FILE = BASE_DIR / "rr.sql"


def initialize_database(db_path: Path, sql_path: Path) -> None:
    """Create the SQLite database and run the SQL script."""
    script = sql_path.read_text(encoding="utf-8")
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        try:
            cursor.executescript(script)
            conn.commit()
        except sqlite3.OperationalError as error:
            message = str(error).lower()
            if "already exists" in message or "table ram" in message:
                print("Database already initialized or table already exists.\n")
            else:
                raise


def query_ram(db_path: Path) -> list[tuple]:
    """Query the ram table and return all rows."""
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, age FROM ram")
        return cursor.fetchall()


def main() -> None:
    if not SQL_FILE.exists():
        raise FileNotFoundError(f"SQL file not found: {SQL_FILE}")

    initialize_database(DB_FILE, SQL_FILE)
    rows = query_ram(DB_FILE)

    print("Connected to SQLite database:", DB_FILE)
    print("ram rows:")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
