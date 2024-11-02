import sqlite3
import json

class CulturalDatabase:
    def __init__(self, db_name='cultural_context.db'):
        """Initialize the cultural database."""
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        """Create tables for storing cultural data."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cultures (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE,
                description TEXT,
                customs TEXT,
                values TEXT
            )
        ''')
        self.connection.commit()

    def add_culture(self, name, description, customs, values):
        """Add a new culture to the database."""
        self.cursor.execute('''
            INSERT INTO cultures (name, description, customs, values)
            VALUES (?, ?, ?, ?)
        ''', (name, description, customs, values))
        self.connection.commit()

    def get_culture(self, name):
        """Retrieve culture information by name."""
        self.cursor.execute('SELECT * FROM cultures WHERE name = ?', (name,))
        return self.cursor.fetchone()

    def update_culture(self, name, description=None, customs=None, values=None):
        """Update existing culture information."""
        updates = []
        if description:
            updates.append(f"description = '{description}'")
        if customs:
            updates.append(f"customs = '{customs}'")
        if values:
            updates.append(f"values = '{values}'")
        
        if updates:
            update_str = ', '.join(updates)
            self.cursor.execute(f'''
                UPDATE cultures SET {update_str} WHERE name = ?
            ''', (name,))
            self.connection.commit()

    def delete_culture(self, name):
        """Delete a culture from the database."""
        self.cursor.execute('DELETE FROM cultures WHERE name = ?', (name,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()
