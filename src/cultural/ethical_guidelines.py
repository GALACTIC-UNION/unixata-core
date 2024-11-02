import json
import logging
from typing import List, Dict, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EthicalGuidelines:
    def __init__(self):
        """Initialize ethical communication guidelines."""
        self.guidelines: List[Dict[str, Any]] = []

    def add_guideline(self, guideline: str, category: Optional[str] = None):
        """Add a new ethical guideline with an optional category."""
        new_guideline = {
            'guideline': guideline,
            'category': category
        }
        self.guidelines.append(new_guideline)
        logging.info(f"Added new guideline: '{guideline}'.")

    def remove_guideline(self, guideline: str):
        """Remove an ethical guideline by its text."""
        for g in self.guidelines:
            if g['guideline'] == guideline:
                self.guidelines.remove(g)
                logging.info(f"Removed guideline: '{guideline}'.")
                return
        logging.error(f"Guideline '{guideline}' not found for removal.")

    def update_guideline(self, old_guideline: str, new_guideline: str, category: Optional[str] = None):
        """Update an existing ethical guideline."""
        for g in self.guidelines:
            if g['guideline'] == old_guideline:
                g['guideline'] = new_guideline
                if category:
                    g['category'] = category
                logging.info(f"Updated guideline from '{old_guideline}' to '{new_guideline}'.")
                return
        logging.error(f"Guideline '{old_guideline}' not found for update.")

    def list_guidelines(self) -> List[Dict[str, Any]]:
        """List all ethical guidelines."""
        return self.guidelines

    def export_to_json(self, file_path: str):
        """Export the ethical guidelines to a JSON file."""
        with open(file_path, 'w') as json_file:
            json.dump(self.guidelines, json_file, indent=4)
        logging.info(f"Exported guidelines to '{file_path}'.")

    def import_from_json(self, file_path: str):
        """Import ethical guidelines from a JSON file."""
        with open(file_path, 'r') as json_file:
            imported_guidelines = json.load(json_file)
            for guideline in imported_guidelines:
                self.add_guideline(guideline['guideline'], guideline.get('category'))
        logging.info(f"Imported guidelines from '{file_path}'.")

    def display_guidelines(self):
        """Display all ethical guidelines in a formatted manner."""
        if not self.guidelines:
            print("No ethical guidelines available.")
            return
        for idx, g in enumerate(self.guidelines, start=1):
            category_info = f" (Category: {g['category']})" if g['category'] else ""
            print(f"{idx}. {g['guideline']}{category_info}")
