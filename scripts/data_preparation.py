# data_preparation.py

import pandas as pd

def load_data(file_path):
    """Load data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def preprocess_data(data):
    """Preprocess the data (e.g., cleaning, normalization)."""
    # Example: Drop missing values
    data = data.dropna()

    # Example: Normalize text data (if applicable)
    data['text'] = data['text'].str.lower()  # Assuming there's a 'text' column

    return data

def save_prepared_data(data, output_path):
    """Save the prepared data to a new CSV file."""
    data.to_csv(output_path, index=False)

def main():
    """Main function to execute data preparation."""
    input_file = 'data/raw_data.csv'  # Adjust input file path as needed
    output_file = 'data/prepared_data.csv'  # Adjust output file path as needed

    # Load, preprocess, and save data
    data = load_data(input_file)
    prepared_data = preprocess_data(data)
    save_prepared_data(prepared_data, output_file)

    print(f"Data preparation completed. Prepared data saved to {output_file}.")

if __name__ == "__main__":
    main()
