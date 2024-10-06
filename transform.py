import pandas as pd

def clean_and_add_column(input_file, output_file, column_name):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Extract the specified column
    original_column = df[column_name]
    
    # Clean the data by removing '-' and 'e'
    cleaned_column = original_column.str.replace('-', '').str.replace('e', '')
    
    # Add the cleaned data as a new column
    df[f'cleaned_{column_name}'] = cleaned_column
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'
column_to_clean = 'your_column_name'

clean_and_add_column(input_file, output_file, column_to_clean)
