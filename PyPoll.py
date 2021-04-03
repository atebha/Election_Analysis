#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. The complete list of canidates who recieved votes.
# 3. The percentage of votes each canidate won.
# 4. The total number of votes each candiate won.
# 5. The winner of the election based on popular vote.

file_to_load = "/Users/farzanasiddiqui/Desktop/Data/Election_Analysis/Resources/election_results.csv"
ed = "file_to_load"
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
ed = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("/Users/farzanasiddiqui/Desktop/Data/Election_Analysis/election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Candidate Opitions and canidate votes
candidate_opitions = []
candidate_votes = {}

# Create a county list and votes dictionary
county_options = []
county_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest county and voter turnout Tracker
county_turnout = ""
county_count = 0
county_tpercentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # To do:read and analyze the data here:

    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Print the canidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row
        county_name = row[1]

        # If the candidate doesn't match any existing canidate.
        if candidate_name not in candidate_opitions:
            # Add it to the list of canidates
            candidate_opitions.append(candidate_name)

            # Begin tracking that canidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that canidate's count.
        candidate_votes[candidate_name] += 1

        # If the county doesn't match any existing county.
        if county_name not in county_options:
            # Add it to the list of counties
            county_options.append(county_name)

            # Track county votes
            county_votes[county_name] = 0

        # Add to county vote count
        county_votes[county_name] += 1

# Save the results to txt file.
with open(file_to_save, "w") as txt_file:

    # Print count to terminal
    election_result = (
        f"\nElection Result\n"
        f"----------------------\n"
        f"Total Votes: {total_votes}\n"
        f"----------------------\n\n"
        f"County Votes:\n")
    print(election_result, end = "")

    txt_file.write(election_result)

    # Determine the percentage of votes for each county by looping through the counts.
    #Iterate through the county list.
    for county_name in county_votes:
        # Retrieve vote count
        covotes = county_votes[county_name]
        # % of total votes for the county
        county_percentage = float(covotes) / float(total_votes) * 100
        county_results = (f"{county_name}: {county_percentage:.1f}% ({covotes:,})\n")

        # Print county result
        print(county_results)

        # Save results to txt file.
        txt_file.write(county_results)

        # Determine largest county turnout and its vote tally
        if (covotes > county_count) and (county_percentage > county_tpercentage):
            county_count = covotes
            county_tpercentage = county_percentage
            county_turnout = county_name

    # Print the largest turnedout county
    county_tpercentage_summary = (
        f"\n-------------------------\n"
        f"Largest County Turnout: {county_tpercentage}\n"
        f"-------------------------\n")
    print(county_tpercentage_summary)

    # Save largest turned out county to txt file.
    txt_file.write(county_tpercentage_summary)

    # Determine the percentage of votes for each canidate by looping through the counts.
    #Iterate through the canidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage of a canidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        candidate_result = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_result)

        # Save all candidates vot tally and % to txt file.
        txt_file.write(candidate_result)

        # Determine winning vote count and canidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            # If true then set winning count = votes and winning percent = vote percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning_canidate equal to the canidate's name.
            winning_candidate = candidate_name
                
    # To do: print out the winning canidate, vote count and percentage to terminal.        
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"               
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary)

    # Save winner's name to txt file.
    txt_file.write(winning_candidate_summary)

    # Close the file.
    election_data.close()