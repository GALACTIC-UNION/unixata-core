import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeedbackLoop:
    def __init__(self, feedback_file='user_feedback.json'):
        """Initialize the feedback loop."""
        self.feedback_file = feedback_file
        self.feedback_data = self.load_feedback()
        logging.info("Feedback loop initialized.")

    def load_feedback(self):
        """Load user feedback from a JSON file."""
        try:
            with open(self.feedback_file, 'r') as file:
                logging.info("Loaded user feedback from file.")
                return json.load(file)
        except FileNotFoundError:
            logging.warning("Feedback file not found. Starting with an empty feedback list.")
            return []

    def save_feedback(self):
        """Save user feedback to a JSON file."""
        with open(self.feedback_file, 'w') as file:
            json.dump(self.feedback_data, file, indent=4)
            logging.info("Saved user feedback to file.")

    def add_feedback(self, user_id: str, feedback: str):
        """Add user feedback to the feedback list."""
        self.feedback_data.append({'user_id': user_id, 'feedback': feedback})
        self.save_feedback()
        logging.info(f"Added feedback from user {user_id}: '{feedback}'.")

    def analyze_feedback(self):
        """Analyze feedback for insights."""
        # Placeholder for analysis logic
        positive_feedback = [f for f in self.feedback_data if 'good' in f['feedback'].lower()]
        negative_feedback = [f for f in self.feedback_data if 'bad' in f['feedback'].lower()]
        logging.info(f"Positive feedback count: {len(positive_feedback)}")
        logging.info(f"Negative feedback count: {len(negative_feedback)}")
        return positive_feedback, negative_feedback

# Example usage
if __name__ == "__main__":
    feedback_loop = FeedbackLoop()
    feedback_loop.add_feedback("user_1", "The translation was good!")
    feedback_loop.add_feedback("user_2", "The translation was bad.")
    feedback_loop.analyze_feedback()
