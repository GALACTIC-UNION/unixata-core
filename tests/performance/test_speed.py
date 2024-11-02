import time
import unittest
from some_module import SomeFunction  # Replace with your actual function/module

class TestSpeed(unittest.TestCase):
    def test_function_speed(self):
        """Test the speed of a specific function."""
        start_time = time.time()
        result = SomeFunction()  # Call the function you want to test
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.6f} seconds")
        
        # Assert that the execution time is within acceptable limits
        self.assertLess(execution_time, 1.0)  # Adjust the threshold as needed

    def test_large_data_processing_speed(self):
        """Test the speed of processing large datasets."""
        large_data = [i for i in range(10**6)]  # Example of large data
        start_time = time.time()
        result = SomeFunction(large_data)  # Call the function with large data
        end_time = time.time()
        
        execution_time = end_time - start_time
        print(f"Large data processing time: {execution_time:.6f} seconds")
        
        # Assert that the execution time is within acceptable limits
        self.assertLess(execution_time, 2.0)  # Adjust the threshold as needed

if __name__ == "__main__":
    unittest.main()
