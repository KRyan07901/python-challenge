# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

with open('election_data..csv') as file:
 csv_reader_object = csv.reader(file)
    
 # Use return number of lines method   
csv_reader_object.line_num
# Count # of votes
count_of_votes = 0
with open('election_data..csv') as file:
    csv_reader_object = csv.reader(file)
    if csv.Sniffer().has_header:
        next(csv_reader_object)
    for row in csv_reader_object:
        count_of_votes+= 1
count_of_votes
print("Election Results")
print("----------------------")
print(f"Total Votes:",count_of_votes)
