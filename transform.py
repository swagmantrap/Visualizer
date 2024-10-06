import csv

def clean_csv_data(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Write header
        writer.writerow(['Original', 'Cleaned'])
        
        for row in reader:
            cleaned_row = []
            for value in row:
                # Convert to string (in case it's not already)
                str_value = str(value).strip()
                # Remove 'e' and '-'
                cleaned_value = str_value.replace('e', '').replace('-', '')
                cleaned_row.append(cleaned_value)
            
            # Write original and cleaned values in a single row
            writer.writerow([', '.join(row), ', '.join(cleaned_row)])

# Example usage
input_file = 'input.csv'
output_file = 'output.csv'

clean_csv_data(input_file, output_file)

print(f"Processed data saved to {output_file}")

# Optionally, read and print the result
with open(output_file, 'r') as file:
    print(file.read())
