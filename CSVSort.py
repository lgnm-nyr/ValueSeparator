# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 11:24:29 2023

@author: amang
"""

import csv

# input and output file paths
input_file = 'Example_Demo.csv'
output_file = 'ExampleDemo0.csv'

# open input and output files
with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # loop through each row in the input file
    for row in reader:
        # check if the third column has a value of 50
        if row[3] == '50':
            # move the row to the output file
            writer.writerow(row)
