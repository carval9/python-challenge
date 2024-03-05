import os
import csv

#Path to collect data from the Resources folder
election_csv = os.path.join('Resources', 'election_data.csv')

#Path for the output file
output_path = os.path.join("analysis","Analysis.csv")

with open(election_csv,'r') as csvfile:
    #Initialize variables
    total_votes = 0
    candidate_list = []
    charles_votes = 0
    diana_votes = 0
    raymon_votes = 0
    charles_per = 0
    diana_per = 0
    raymon_per = 0
    winner = []
    max_per = 0
    winner_index = 0

    #Read the file
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip the file headers
    header=next(csvreader)

    for row in csvreader:
        #Calculate total count of votes
        total_votes += 1

        #Get the list of candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])

        #Get the amount of votes per candidate
        if row[2] == "Charles Casper Stockham":
            charles_votes += 1

        if row[2] == "Diana DeGette":
            diana_votes += 1

        if row[2] == "Raymon Anthony Doane":
            raymon_votes += 1

#Get the percentage of votes per candidate
charles_per = (charles_votes*100)/total_votes
diana_per = (diana_votes*100)/total_votes
raymon_per = (raymon_votes*100)/total_votes

#Add format to percentage values
charles_per = format(charles_per,".3f")
diana_per = format(diana_per,".3f")
raymon_per = format(raymon_per,".3f")

#Get winner
winner = [charles_per,diana_per,raymon_per]
#This line was taken from URL
#https://www.tutorialspoint.com/python/list_max.htm
max_per = max(winner)
winner_index = winner.index(max_per)
winner = candidate_list[winner_index]

#Print in terminal results
print(f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------""")
print(f"{candidate_list[0]}: {charles_per}% ({charles_votes})")
print(f"{candidate_list[1]}: {diana_per}% ({diana_votes})")
print(f"{candidate_list[2]}: {raymon_per}% ({raymon_votes})")
print(f"""-------------------------
Winner: {winner}
-------------------------""")

#Print in the output file
with open(output_path,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"{candidate_list[0]}: {charles_per}% ({charles_votes})"])
    csvwriter.writerow([f"{candidate_list[1]}: {diana_per}% ({diana_votes})"])
    csvwriter.writerow([f"{candidate_list[2]}: {raymon_per}% ({raymon_votes})"])
    csvwriter.writerow(["-------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["-------------------------"])