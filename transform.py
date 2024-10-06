import pandas as pd
import numpy as np

def clean_scientific_notation(input_file, output_file, column_name):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Extract the specified column
    original_column = df[column_name]
    
    def process_number(x):
        # Convert to float to handle scientific notation
        num = float(x)
        # Take absolute value to remove negative sign
        num = abs(num)
        # Convert to string with fixed notation
        return f"{num:.16f}".rstrip('0').rstrip('.')
    
    # Apply the processing function to each element
    cleaned_column = original_column.apply(process_number)
    
    # Add the cleaned data as a new column
    df[f'cleaned_{column_name}'] = cleaned_column
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'
column_to_clean = 'your_column_name'

clean_scientific_notation(input_file, output_file, column_to_clean)
