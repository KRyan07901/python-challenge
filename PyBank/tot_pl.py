import os
import csv

# Open the CSV
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
# Set Total Net P&L Variable to 0 in order to sum each record
    x = 0
# Loop through the csv file
    for row in csvreader:
        x = x + int(row[1]) 
        print(f"{x}")