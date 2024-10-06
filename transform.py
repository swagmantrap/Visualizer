import pandas as pd
import numpy as np

def clean_and_add_numerical_column(input_file, output_file, column_name):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Extract the specified column
    original_column = df[column_name]
    
    # Convert to float to handle scientific notation
    numerical_column = pd.to_numeric(original_column, errors='coerce')
    
    # Remove scientific notation
    cleaned_column = numerical_column.apply(lambda x: f"{x:.10f}" if pd.notnull(x) else x)
    
    # Remove trailing zeros after decimal point
    cleaned_column = cleaned_column.apply(lambda x: x.rstrip('0').rstrip('.') if isinstance(x, str) else x)
    
    # Add the cleaned data as a new column
    df[f'cleaned_{column_name}'] = cleaned_column
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'
column_to_clean = 'your_column_name'

clean_and_add_numerical_column(input_file, output_file, column_to_clean)
