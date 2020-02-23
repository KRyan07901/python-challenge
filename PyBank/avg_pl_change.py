import os
import csv

# Open the CSV
with open("budget_data.csv", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
# Set Average Monthly P&L Change variable.  Average Monthly Change = Current Month - Prior Month.  Stated 
# another way Months 1-86.  Start with Month 2 - Month 1 than iterate adding 1 to each variable.

# Loop through the csv file
for row in csvreader:
        cur_month= row[1]
        print(cur_month)
