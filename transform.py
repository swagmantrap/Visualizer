import pandas as pd
import numpy as np

def clean_scientific_notation(input_file, output_file):
    # Read the CSV file
    with open(input_file, 'r') as file:
        data = file.read().strip()
    
    # Split the data into individual numbers
    numbers = [num.strip() for num in data.split(',')]
    
    def process_number(x):
        # Convert to float to handle scientific notation
        num = float(x)
        # Take absolute value to remove negative sign
        num = abs(num)
        # Convert to string with fixed notation
        return f"{num:.16f}".rstrip('0').rstrip('.')
    
    # Apply the processing function to each number
    cleaned_numbers = [process_number(num) for num in numbers]
    
    # Create a DataFrame with the original and cleaned data
    df = pd.DataFrame({
        'original': numbers,
        'cleaned': cleaned_numbers
    })
    
    # Save the DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")
    return df

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'

result = clean_scientific_notation(input_file, output_file)
print(result)
