file_to_load = '/Users/farzanasiddiqui/Desktop/Data/Election_Analysis//Resources/election_results.csv'
ed = "file_to_load"
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
ed = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("election_analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # To do:read and analyze the data here:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# To do: Perform Analysis


# Close the file.
#election_data.close()