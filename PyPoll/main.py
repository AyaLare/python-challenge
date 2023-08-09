
import os
import csv 
# Author: Foluke Daramola
#  This Python script will analyze data in Election_data.csv, calculate,display and print thefollowing values
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the lection based on populare votes

def main():
   #
   # Defining the key variables required for the analysis
   #
    row_count = 0
    current_candidate_voted = " "
    candidate_ballot = 0
    candidate_count = 0
    candidate = "  "
    previous_candidate_total = 0
    #vote_count = 0
    total_number_of_votes_cast = 0
    ballot_id = 0
    ballot_county = " "
    ballot_voted_for = " "
    #List_of_candidates_received_votes = []
    #Percentage_votes_per_candidate = [ ]
    #Total_number_votes_per_candidate = 0
    #Winner_of_election_based_on_popular_vote = ""
    #
    # Creating the election result dictionary
    #
    election_dictionary = {}
    # 
    # Defining the path to the source data file to be analyzed
    #       
    csvpath = os.path.join("..","PyPoll\Resources", "election_data.csv")
    #
    # Define the file where the result of the analysis will be stored
    #
    output_path = os.path.join("..","PyPoll\Analysis", "PyPoll Election Result.txt")
    with open(csvpath) as csvfile:
#          # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
         #
         # Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
         # print(csv_header)
         #        
         # Read each row of data after the header
         #
        election_dictionary = {" ", 0}
        for row in csvreader:
            row_count = row_count + 1
            ballot_id = int(row[0])
            ballot_county = row[1]
            ballot_voted_for = row[2]
            if row[2] == current_candidate_voted:
                candidate_ballot = candidate_ballot + 1
            
            if row[2] != current_candidate_voted:
               candidate_count = candidate_count + 1
               if row[2] not in election_dictionary:
                    print(str(row[2]))
                    candidate = row[2]
                    election_dictionary.update({candidate: candidate_ballot})
                    print(election_dictionary)
               else:
                    #previous_candidate_total = election_dictionary[candidate_count]  
                    previous_candidate_total = previous_candidate_total + candidate_ballot
                    print(previous_candidate_total)
                    election_dictionary.update({candidate_count: previous_candidate_total})
                    print(election_dictionary)
                     #election_dictionary.add(row[2]: previous_candidate_total)
                    candidate_ballot = 1
                    current_candidate_voted = row[2]
            #print(str(ballot_id) + " " + ballot_county + " " + ballot_voted_for)
            # Update the dictionary
            # election_dictionary[str(row[2])] = row[2]
            #election_dictionary
    print(election_dictionary) 
   # Generate and print the summary information from the data
   # 
    total_number_of_votes_cast = row_count        
    print("Election Results")
    print("_____________________________________")
    print("Total Votes: " + str(total_number_of_votes_cast))
    print("_____________________________________")
   #
   # open the file and write ther results
   #
    with open(output_path, 'w') as file:
        file.writelines("Election Results" + "\n") 
        file.writelines("_____________________________________" + "\n") 
        file.writelines("Total Months: " + str(total_number_of_votes_cast) + "\n")
        file.writelines("_____________________________________" + "\n")
main()