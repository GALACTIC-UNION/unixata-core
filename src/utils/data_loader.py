import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, file_path: str):
        """Initialize the DataLoader with a file path."""
        self.file_path = file_path
        self.data = None

    def load_data(self):
        """Load data from a CSV file."""
        try:
            self.data = pd.read_csv(self.file_path)
            print(f"Data loaded successfully from {self.file_path}.")
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} was not found.")
        except pd.errors.EmptyDataError:
            print("Error: The file is empty.")
        except pd.errors.ParserError:
            print("Error: The file could not be parsed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def preprocess_data(self):
        """Preprocess the data (placeholder for actual preprocessing steps)."""
        if self.data is not None:
            # Example preprocessing: fill missing values and normalize
            self.data.fillna(self.data.mean(), inplace=True)
            self.data = (self.data - self.data.mean()) / self.data.std()
            print("Data preprocessed successfully.")
        else:
            print("No data to preprocess. Please load data first.")

    def get_data(self):
        """Return the preprocessed data."""
        if self.data is not None:
            return self.data
        else:
            print("No data available. Please load data first.")
            return None

# Example usage
if __name__ == "__main__":
    # Specify the path to your CSV file
    file_path = 'data/sample_data.csv'  # Change this to your actual file path
    data_loader = DataLoader(file_path)
    
    data_loader.load_data()  # Load the data
    data_loader.preprocess_data()  # Preprocess the data
    
    # Retrieve the preprocessed data
    preprocessed_data = data_loader.get_data()
    if preprocessed_data is not None:
        print(preprocessed_data.head())  # Display the first few rows of the preprocessed data
