import pandas as pd

def clean_csv_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file, header=None)
    
    # Rename the column(s)
    df.columns = ['Original']
    
    # Function to clean each value
    def clean_value(value):
        return str(value).replace('e', '').replace('-', '')
    
    # Apply the cleaning function to create a new 'Cleaned' column
    df['Cleaned'] = df['Original'].apply(clean_value)
    
    # Save the result to a new CSV file
    df.to_csv(output_file, index=False)
    
    print(f"Processed data saved to {output_file}")
    return df

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'

result = clean_csv_data(input_file, output_file)
print(result)
