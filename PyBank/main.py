#
# Module 3 Challenge
#
# PyBank Python Script
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
inputFilePath = os.path.join(".", "Resources", "budget_data.csv")

# Set path for text output Analysis file
outputFilePath = os.path.join(".", "Analysis", "PyBank_Analysis.txt")

# initialize variables
recordCount = 0
recordTotal = 0
#
max_change = 0
max_change_date = None
min_change = 0
min_change_date = None
#
changeCount   = 0
changeTotal   = 0
changeAverage = 0
#
output = ""

# Open the CSV using ascii encoding
with open(inputFilePath, "r", encoding='ascii') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row and ignore
    store_csv_header = next(csvreader)

    # initialize variable - this is the Profit/Loss value that drives the "change" calculation between file rows
    prev_profit_loss = None

    # Read each row of data after the header
    for row in csvreader:
        
        # read Date and Profit/Losses values from file row
        date, profit_loss = row
        
        # determine Changes in values
        # NOTE: this "if" block is only be performed on the rows that follow the very first row of data (i.e. "changes" between rows of data)
        if prev_profit_loss is not None:
            # Calculate the change in Profit/Loss from the previously saved Profit/Loss value
            change = int(profit_loss) - int(prev_profit_loss)
            
            # Add to running total s
            changeCount += 1
            changeTotal += change
            
            # this will determine which two Profit/Loss Changes represent the Greatest Increase, and Greatest Decrese
            if change > max_change:
                max_change = change
                max_change_date = date
            if change < min_change:
                min_change = change
                min_change_date = date
        
        # save the current Profit/Loss so it can be compared to the next row (when the "for" loop processes a next row)
        prev_profit_loss = profit_loss

        # increment the running totals
        recordCount += 1
        recordTotal += int(profit_loss) 

# calculate the Average Change
changeAverage = changeTotal/changeCount
    
# assemble all the output to be written
output += "Financial Analysis" + "\n"
output += "----------------------------" + "\n"
output += f"Total Months: {recordCount}" + "\n"
output += f"Total: ${recordTotal:.0f}" + "\n"
output += f"Average Change: ${changeAverage:.2f}" + "\n"
output += f"Greatest Increase in Profits: {max_change_date} (${max_change:.0f})" + "\n"
output += f"Greatest Decrease in Profits: {min_change_date} (${min_change:.0f})" + "\n"

# write output to console screen
print(output)

# Open a file for writing
with open(outputFilePath, "w") as file:
    # write output to file
    file.write(output)
