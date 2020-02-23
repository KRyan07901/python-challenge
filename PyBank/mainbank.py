# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

with open('budget_data.csv') as file:
    csv_reader_object = csv.reader(file)
    
 # Use return number of lines method   
csv_reader_object.line_num
# Count # of months
count_of_months = 0
with open('budget_data.csv') as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    for row in csv_reader_object:
        count_of_months += 1
count_of_months
print("Financial Analysis")
print("----------------------")
print(f"Total Months:",count_of_months)
