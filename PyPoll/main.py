import csv
import os

file_to_open = os.path.join("Resources", "election_data.csv")
with open(file_to_open) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")

    header = next(csvreader)
    print(header)

    count = 0
    total_votes = 0
    candidate_list = []
    eachtotal = 0
    candidates = {"Charles Casper Stockham":3,
                    "Diana DeGette":2,
                    "Raymon Anthony Doane":1}

    for row in csvreader:
        count = count + 1
        total_votes = total_votes + 1
        
        if candidates not in candidate_list:
            candidate_list.append(row[0]) 
             #candidates[row[0]] = 1
             #percentage = count/total_votes
        #candidates[row[0]] = candidates[row[0]] + 1   

        
    print(f"Total Votes: {total_votes}")
    print(candidate_list)
    print(eachtotal)
    print(candidates)

output_path = os.path.join("analysis", "Analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write(f"Total votes = {total_votes}")
   # txtfile.write(f"candidate_list)
    #txtfile.write(eachtotal)
    #txtfile.write(candidates)
