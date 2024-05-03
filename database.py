import sqlite3


def connect_to_database():
    return sqlite3.connect("subsidiaries.db")


def create_database_table(db_cursor):
    db_cursor.execute("""
        CREATE TABLE IF NOT EXISTS subsidiaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT,
            name TEXT,
            UNIQUE(company_name, name) 
        )
    """)


def check_subsidiary_exists(db_cursor, subsidiary_name):
    db_cursor.execute("""
        SELECT EXISTS(SELECT 1 FROM subsidiaries WHERE name=? LIMIT 1)
    """, (subsidiary_name,))
    return db_cursor.fetchone()[0] == 1  # More efficient existence check


def add_new_subsidiary(db_cursor, company_name, subsidiary_name):
    try:
        db_cursor.execute("""
            INSERT INTO subsidiaries (company_name, name) VALUES (?, ?)
        """, (company_name, subsidiary_name))
    except sqlite3.IntegrityError:
        print(f"Subsidiary or company ({company_name}, {subsidiary_name}) already exists.")
        # Optionally add logic to update the entry if desired


def update_subsidiary(db_cursor, old_name, new_name):
    db_cursor.execute("""
         UPDATE subsidiaries SET name = ? WHERE name = ?
     """, (new_name, old_name))
