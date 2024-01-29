import csv

# Open the input CSV file
with open('testres2.0v2.csv', 'r') as input_file:
    reader = csv.reader(input_file)

    # Create a dictionary to hold the counts of each value
    counts = {}

    # Iterate over each row in the CSV file
    for row in reader:
        # Get the value from the third column
        value = row[2]

        # If the value is not already in the dictionary, add it with a count of 1
        if value not in counts:
            counts[value] = 1
        # If the value is already in the dictionary, increment its count
        else:
            counts[value] += 1

# Open the output CSV file
with open('res2.0comcountv2.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)

    # Write the number of unique values to the first row
    writer.writerow(['Number of unique values:', len(counts)])

    # Write the counts of each value to subsequent rows
    for value, count in counts.items():
        writer.writerow([value, count])
