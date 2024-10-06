import pandas as pd

def clean_csv_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Get the name of the third column
    third_column_name = df.columns[2]
    
    # Function to clean each value
    def clean_value(value):
        return str(value).replace('e', '').replace('-', '')
    
    # Apply the cleaning function to create a new column
    new_column_name = f'Cleaned_{third_column_name}'
    df[new_column_name] = df[third_column_name].apply(clean_value)
    
    # Save the result to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")
    return df

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'

result = clean_csv_data(input_file, output_file)
print(result)
