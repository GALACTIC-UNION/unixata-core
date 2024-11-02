import sqlite3
import json
from typing import List, Dict, Any, Optional

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
                values TEXT,
                language TEXT,
                region TEXT,
                traditions TEXT
            )
        ''')
        self.connection.commit()

    def add_culture(self, name: str, description: str, customs: str, values: str, 
                    language: Optional[str] = None, region: Optional[str] = None, 
                    traditions: Optional[str] = None):
        """Add a new culture to the database."""
        try:
            self.cursor.execute('''
                INSERT INTO cultures (name, description, customs, values, language, region, traditions)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (name, description, customs, values, language, region, traditions))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Culture '{name}' already exists in the database.")

    def get_culture(self, name: str) -> Optional[Dict[str, Any]]:
        """Retrieve culture information by name."""
        self.cursor.execute('SELECT * FROM cultures WHERE name = ?', (name,))
        row = self.cursor.fetchone()
        if row:
            return {
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'customs': row[3],
                'values': row[4],
                'language': row[5],
                'region': row[6],
                'traditions': row[7]
            }
        return None

    def update_culture(self, name: str, description: Optional[str] = None, customs: Optional[str] = None, 
                       values: Optional[str] = None, language: Optional[str] = None, 
                       region: Optional[str] = None, traditions: Optional[str] = None):
        """Update existing culture information."""
        updates = []
        if description:
            updates.append(f"description = '{description}'")
        if customs:
            updates.append(f"customs = '{customs}'")
        if values:
            updates.append(f"values = '{values}'")
        if language:
            updates.append(f"language = '{language}'")
        if region:
            updates.append(f"region = '{region}'")
        if traditions:
            updates.append(f"traditions = '{traditions}'")
        
        if updates:
            update_str = ', '.join(updates)
            self.cursor.execute(f'''
                UPDATE cultures SET {update_str} WHERE name = ?
            ''', (name,))
            self.connection.commit()

    def delete_culture(self, name: str):
        """Delete a culture from the database."""
        self.cursor.execute('DELETE FROM cultures WHERE name = ?', (name,))
        self.connection.commit()

    def list_cultures(self) -> List[Dict[str, Any]]:
        """List all cultures in the database."""
        self.cursor.execute('SELECT * FROM cultures')
        rows = self.cursor.fetchall()
        return [{
            'id': row[0],
            'name': row[1],
            'description': row[2],
            'customs': row[3],
            'values': row[4],
            'language': row[5],
            'region': row[6],
            'traditions': row[7]
        } for row in rows]

    def export_to_json(self, file_path: str):
        """Export the cultural data to a JSON file."""
        cultures = self.list_cultures()
        with open(file_path, 'w') as json_file:
            json.dump(cultures, json_file, indent=4)

    def import_from_json(self, file_path: str):
        """Import cultural data from a JSON file."""
        with open(file_path, 'r') as json_file:
            cultures = json.load(json_file)
            for culture in cultures:
                self.add_culture(
                    name=culture['name'],
                    description=culture['description'],
                    customs=culture['customs'],
                    values=culture['values'],
                    language=culture.get('language'),
                    region=culture.get('region'),
                    traditions=culture.get('traditions')
                )

    def close(self):
        """Close the database connection."""
        self.connection.close()
