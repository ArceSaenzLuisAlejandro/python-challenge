import os
import csv
from collections import defaultdict
# -----------------PyPoll-----------------
csv_path = os.path.join("election_data.csv")

votes_counter = 0
candidates = []
vote_sum = [0,0,0,0]
percentage = []
print_results = []

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip headers
    next(csvreader, None)
    # Headers: "Date", "Profit/Losses"
    
    for row in csvreader:
        # Votes counter
        votes_counter += 1
        # Appennd candidates on a list
        if row[2] not in candidates:
            candidates.append(row[2])        
        # Sum total votes for each candidate
        for i in candidates:
            if i == row[2]:
                vote_sum[candidates.index(i)] = vote_sum[candidates.index(i)] + 1
    for i in vote_sum:
        percentage.append(i/votes_counter*100)
            
print("Election Results" +
      "\n------------------" +
      "\nTotal Votes: " + str(votes_counter) +
      "\n------------------"
     )
for i in candidates:
          print_results.append(str(i) + ": " + 
          str(percentage[candidates.index(i)]) + "% " +
          "(" + str(vote_sum[candidates.index(i)]) + ")"
                )
x = str([print(i) for i in print_results])
print("------------------" +
      "\nWinner: " + str(candidates[percentage.index(max(percentage))])
      + "\n------------------" 
     )

file_txt = open("Election_Data.txt","w") 
write = ["Election Results",
        "\n------------------",
        "\nTotal Votes: ", str(votes_counter),
        "\n------------------\n",
        str([i for i in print_results]),
        "\n------------------",
        "\nWinner: ",
        str(candidates[percentage.index(max(percentage))]),
        "\n------------------"
        ]  
file_txt.writelines(write) 
file_txt.close()