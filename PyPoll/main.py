# PyPoll retuns the results of the election including: each candidate receiving votes, the pecent of the vote received,
# the total votes received and the Winner, from data set elecetion data.csv

# Import lib for .csv file handling 
import csv
# Import lib for os path handling 
import os

# Set paths for input csv and output txt
path = os.path.join("Resources","election_data.csv")
analysis_path = os.path.join("Analysis","ElectionAnalysis.txt")

# initialize row count to zero and create dictionary Votes to hold summary
row_count = 0
Votes = {}

with open(path) as election_data:
    ed = csv.reader(election_data, delimiter=',')

    Header =  next(ed) # Skip header row 
    first = True # Set flag for first row 
 
    # Iterate through file and store results in dictionary Votes
    for row in ed:
        candidate_name = (row[2])
        candidate_count = 1
        if first:    # fisrt time through set inital values for counts and dictionary 
            total_votes = 1
            new_dict_candidate = {candidate_name : candidate_count}
            Votes.update(new_dict_candidate)
            first = False
        else:        # Process rest of vote data
            if candidate_name in Votes:
                 candidate_count = (int(Votes[candidate_name]) + 1)
            Votes.update({candidate_name : candidate_count})
            total_votes += 1
              

# Build results list
line = ('-' *25) # define separater line for input 
results = [f'Election Results',line,f'Total votes =  {total_votes}',line,] # Set title 

# iterate through dictionary to build results 
winner_percent = 0.0  # Cast winner percent as float

for key in Votes:
    current_percent = float((Votes[key]) / total_votes) * 100
    results.append(f'{key}: {round(current_percent,2)}% {Votes[key]}') # Add next candidate
    # Check to see if this candidate is the winner
    if current_percent > winner_percent:
        winner_percent = current_percent
        winner = key
# Add winner to results 
results.append(line)
results.append(winner)
results.append(line)

# print results to Terminal
print('\n'.join(results))

# Write results to .txt file 
with open(analysis_path, 'w') as analysis:
    analysis.write('\n'.join(results))

