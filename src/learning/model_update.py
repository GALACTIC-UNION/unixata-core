import logging
import time
from feedback_loop import FeedbackLoop
from continuous_learning import ContinuousLearning

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ModelUpdater:
    def __init__(self, feedback_loop: FeedbackLoop, continuous_learning: ContinuousLearning):
        """Initialize the model updater."""
        self.feedback_loop = feedback_loop
        self.continuous_learning = continuous_learning
        logging.info("Model updater initialized.")

    def check_for_updates(self):
        """Check for new feedback and update the model if necessary."""
        while True:
            logging.info("Checking for new feedback...")
            feedback_data = self.feedback_loop.feedback_data
            
            if feedback_data:
                logging.info(f"Found {len(feedback_data)} feedback entries.")
                self.continuous_learning.update_model(feedback_data)
                self.feedback_loop.save_feedback()  # Save feedback after processing
            else:
                logging.info("No new feedback found.")

            time.sleep(60)  # Check for updates every minute

    def retrain_model(self):
        """Retrain the model based on accumulated feedback."""
        logging.info("Retraining model...")
        self.continuous_learning.retrain_model()
        logging.info("Model retraining completed.")

# Example usage
if __name__ == "__main__":
    feedback_loop = FeedbackLoop()
    continuous_learning = ContinuousLearning()
    model_updater = ModelUpdater(feedback_loop, continuous_learning)

    # Start checking for updates (this will run indefinitely)
    try:
        model_updater.check_for_updates()
    except KeyboardInterrupt:
        logging.info("Model updater stopped by user.")
