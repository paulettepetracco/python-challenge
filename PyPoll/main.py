import os
import csv


#Store filepath in a variable
election_data = os.path.join("r'//Users/paulettepetracco/Bootcamp_Code_Challenges/GH_Repositories/python-challenge/PyPoll/Resources/election_data.csv")
save_path = "/Users/paulettepetracco/Bootcamp_Code_Challenges/GH_Repositories/python-challenge/PyPoll"
completeName = os.path.join(save_path, "output.txt")

# variables
TotalVotes = 0
candidateNames = []
winner = {}

#pull from the csv file
with open (r'//Users/paulettepetracco/Bootcamp_Code_Challenges/GH_Repositories/python-challenge/PyPoll/Resources/election_data.csv', newline = '') as csvfile:
    election_data = csv.reader(csvfile)

    # find the total number of votes with loop
    for row in election_data: 
    # total number of votes included in the data
        if row[0] == "Ballot ID":continue
        TotalVotes += 1
        candidateNames.append(row[2])
    print("Election Results", file=open(completeName,"a"))
    print("----------------------------", file=open(completeName,"a"))
    print(f"Total Votes: {TotalVotes}", file=open(completeName,"a"))
    print("----------------------------", file=open(completeName,"a"))
        
    candidates = list(set(candidateNames))
    candidates.sort()
    
    for candidate in candidates: 
        name = candidate
        candidateVotes = candidateNames.count(candidate)
        percentage = round((candidateVotes / TotalVotes) * 100, 3)
        
        print(f"{name}: {percentage}% ({candidateVotes})")
        print(f"{name}: {percentage}% ({candidateVotes})", file=open(completeName,"a"))
        
        if not winner: 
            winner["name"] = name 
            winner["votes"] = candidateVotes
        elif candidateVotes > winner["votes"]: winner.update({"name": name, "votes": candidateVotes})
        else: continue
        

    print("----------------------------", file=open(completeName,"a"))
    print(f"Winner: {winner['name']}", file=open(completeName,"a"))



