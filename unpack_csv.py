import csv

# Define the input CSV file and the output file
input_file = 'FeynmanEquations.csv'
output_file = 'FeynmanEquations_cleaned.txt'

# Function to process each row
def process_row(row):
    # Extract the fields from the row
    filename = row[0]
    number = row[1]
    output = row[2]
    formula = row[3]
    num_vars = int(row[4])
    
    variables = []
    for i in range(num_vars):
        var_name = row[5 + i * 3]
        var_low = row[6 + i * 3]
        var_high = row[7 + i * 3]
        variables.append((var_name, var_low, var_high))
    
    return {
        'Filename': filename,
        'Number': number,
        'Output': output,
        'Formula': formula,
        'Variables': variables
    }

# Read the CSV file and write the unpacked data to a text file
with open(input_file, mode='r') as csv_file, open(output_file, mode='w') as output_file:
    csv_reader = csv.reader(csv_file)
    
    # Skip the header row
    next(csv_reader)
    
    for row in csv_reader:
        # Process each row
        data = process_row(row)
        
        # Write data to the output file
        output_file.write(f"Filename: {data['Filename']}\n")
        output_file.write(f"Number: {data['Number']}\n")
        output_file.write(f"Output: {data['Output']}\n")
        output_file.write(f"Formula: {data['Formula']}\n")
        output_file.write("Variables:\n")
        
        for var_name, var_low, var_high in data['Variables']:
            output_file.write(f"  Name: {var_name}, Low: {var_low}, High: {var_high}\n")
        
        output_file.write("\n")

print(f"Data has been unpacked and saved to {output_file.name}.")