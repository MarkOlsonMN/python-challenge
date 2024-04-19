#
# Module 3 Challenge
#
# PyPoll Python Script
#
# Class: U of M Data Analytics and Visualization Boot Camp , Spring 2024
# Student: Mark Olson
# Professor: Thomas Bogue , Assisted by Jordan Tompkins
# Date: 04/18/2024
#

# Module to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Set path for CSV input Data file
inputFilePath = os.path.join(".", "Resources", "election_data.csv")

# Set path for text output Analysis file
outputFilePath = os.path.join(".", "Analysis", "PyPoll_Analysis.txt")

# initial variables
total_Votes = 0
maxValue_Votes = 0
maxKey_Candidate = ""
specialOutput = ""

# Initialize variable - an empty dictionary to store Candidate names and Vote counts
candidateCounts = {}

# Open the CSV using ascii encoding
with open(inputFilePath, "r", encoding='ascii') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row and ignore
    store_csv_header = next(csvreader)

    # define constant - the column offset that hold Candidate name
    ROW_CANDIDATE=2

    # Read each row of data after the header
    for row in csvreader:
        # Add to running total of all Votes that were cast
        total_Votes += 1

        candidateName = row[ROW_CANDIDATE]

        # Add Info from Data file to Dictionary
        if candidateName in candidateCounts:
            # If the Candidate name already exists, increment the Vote count by 1
            candidateCounts[candidateName] += 1
        else:
            # If the Candidate name is not in the dictionary, add it with a Vote count of 1
            candidateCounts[candidateName] = 1


# Iterate over the Dictionary to process the key-value pairs ... Candidate name - Votes count
for key, value in candidateCounts.items():
    currentKey_Candidate = key
    currentValue_Votes = value

    # calculate the percentage of votes a Candiadate recieved out of the total votes that were cast
    current_Percent = (currentValue_Votes/total_Votes)

    # generate "specialOutput" section to be used further below
    specialOutput += f"{currentKey_Candidate}: {current_Percent:.3%} ({currentValue_Votes})" + "\n"

    # this will determine which Candidate had the most Votes
    if currentValue_Votes > maxValue_Votes:
        maxValue_Votes = currentValue_Votes
        maxKey_Candidate = currentKey_Candidate

# assemble all the output to be written
output = ""
output += "Election Results" + "\n"
output += "-------------------------" + "\n"
output += f"Total Votes: {total_Votes}" + "\n"
output += "-------------------------" + "\n"
# include the "specialOutput" section that was generated previously
output += f"{specialOutput}"
output += "-------------------------" + "\n"
output += f"Winner: {maxKey_Candidate}" + "\n"
output += "-------------------------" + "\n"

# write output to console screen
print(output)

# Open a file for writing
with open(outputFilePath, "w") as file:
    # write output to file
    file.write(output)
