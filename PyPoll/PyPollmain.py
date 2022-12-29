import os
import csv

electiondata_csv = os.path.join("Resources", "election_data.csv")
text_file = os.path.join("Analysis", "PyPoll.txt")

#vote counter
total_votes = 0
#counter for winning count
winning_count = 0
#setup sting for winning candidate
winner = ""
names = []
candidate_votes = {}

with open (electiondata_csv, "r") as data:
    reader = csv.reader(data)
    header = next(reader)

    for line in reader:
        total_votes += 1
        candidate_name = line[2]
        if candidate_name not in names:
            names.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

with open (text_file,"w") as outputfile:
    output = f'''
    Election Results
    -------------------------
    Total Votes: {total_votes:,}
    -------------------------
    '''
    print(output)
    outputfile.write(output)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        percent = votes/total_votes*100
        if votes > winning_count:
            winning_count = votes
            winner = candidate
        election_output = f"{candidate}: {percent:.3f}% ({votes:,})\n"
        print(election_output)
        outputfile.write(election_output)
    winning_candidate = f""" 
    -------------------------
    Winner: {winner}
    -------------------------
    """
    print(winning_candidate)
    outputfile.write(winning_candidate)



