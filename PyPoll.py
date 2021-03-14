#The data we need to retrieve.
# 1. The total number of votes cast.
# 2. The complete list of canidates who recieved votes.
# 3. The percentage of votes each canidate won.
# 4. The total number of votes each candiate won.
# 5. The winner of the election based on popular vote.

file_to_load = "/Users/farzanasiddiqui/Desktop/Data/Election_Analysis//Resources/election_results.csv"
ed = "file_to_load"
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
ed = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis", "election_analysis.txt")

# Initialize a total vote counter
total_votes = 0

# Canidate Opitions and canidate votes
canidate_opitions = []
canidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
        canidate_name = row[2]

        # If the canidate doesn't match any existing canidate.
        if canidate_name not in canidate_opitions:
            # Add it to the list of canidates
            canidate_opitions.append(canidate_name)

            # Begin tracking that canidate's vote count.
            canidate_votes[canidate_name] = 0

        # Add a vote to that canidate's count.
        canidate_votes[canidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

        # Determine the percentage of votes for each canidate by looping through the counts.
        # Iterate through the canidate lsit.
    for canidate_name in canidate_votes:
        # Retrieve vote count and percentage of a canidate.
        votes = canidate_votes[canidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        canidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and canidate
    print(canidate_totals)
    # Save results to txt file.
    txt_file.write(canidate_results)

    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):

        # If true then set winning count = votes and winning percent = vote percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # And set the winning_canidate equal to the canidate's name.
        winning_candidate = canidate_name
                
# To do: print out the winning canidate, vote count and percentage to terminal.        
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"               
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    
#print(winning_candidate_summary)

# Close the file.
election_data.close()