
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
    candidate_ballot = 1
    candidate_count = 0
    candidate = "  "
    previous_candidate_total = 0
    total_number_of_votes_cast = 0
    popular_vote = 0
    election_dictionary_keys = []
    #List_of_candidates_received_votes = []
    #Percentage_votes_per_candidate = 0
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
    # CSV reader specifies delimiter and variable that holds contents
        csvreader = csv.reader(csvfile, delimiter=',')
         #
         # Read the header row first (skip this step if there is no header)
        csv_header = next(csvreader)
         # print(csv_header)
         #        
         # Read each row of data after the header
         #
        #election_dictionary = {" ", 0}
        election_dictionary = {}
        for row in csvreader:
            row_count = row_count + 1
            #ballot_id = int(row[0])
            #ballot_county = row[1]
            #
            #Test if the data retrieved is for a different candidate than previously held
            #
            #Candidate is the same, so keep adding the ballots to the ballot count for the candidate
            if row[2] == current_candidate_voted:
                candidate_ballot = candidate_ballot + 1
            #Candidate is now different, so its time write the interim result for the previous candidate in memory
            if row[2] != current_candidate_voted:
               #There is a new candidate, so increase the count
               candidate_count = candidate_count + 1
               #Check if the previous candidate already has votes stored in the election registry and check its not blank (first time)
               if current_candidate_voted not in election_dictionary and current_candidate_voted != " ":
                    #print(current_candidate_voted + "not yet in dictionary")
                    #Write the interim ballot votes for the previous candidate into the registry
                    election_dictionary.update({current_candidate_voted: candidate_ballot})
                    #Check if the candidate's ballot count is the highest so far, if so make it the highest
                    if candidate_ballot > popular_vote:
                        popular_candidate = current_candidate_voted
                        popular_vote = candidate_ballot
               #The candidate already has a previous ballot count in the election registry
               #The ballot count int he registry is to be updated with the interim count recently got
               elif current_candidate_voted != " " :
                    candidate_count = candidate_count - 1
                    previous_candidate_total = election_dictionary.get(current_candidate_voted)  
                    previous_candidate_total = previous_candidate_total + candidate_ballot
                    #print(current_candidate_voted + " Previous Votes: " + str(election_dictionary.get(current_candidate_voted)) + "  Additional Votes: " + str(candidate_ballot) + "  New Total Votes: " + str(previous_candidate_total))
                    election_dictionary.update({current_candidate_voted: previous_candidate_total})
                    #Check if the cumulaative ballot count for the candidate is highest and if so, change the highest score to reflect this info
                    if previous_candidate_total > popular_vote:
                           popular_candidate = current_candidate_voted
                           popular_vote = previous_candidate_total
               #Switch the candidate to the latest data read from the database
               candidate_ballot = 1
               current_candidate_voted = row[2]
        #Update the registry for the last batch of data accumulated and conditionally update the popular vote i.e. the winner info
        previous_candidate_total = election_dictionary.get(current_candidate_voted)  
        previous_candidate_total = previous_candidate_total + candidate_ballot
        election_dictionary.update({current_candidate_voted: previous_candidate_total})
        if previous_candidate_total > popular_vote:
             popular_candidate = current_candidate_voted
        #print(election_dictionary)
   # Generate and print the analysis summary information to the screen
   # 
    total_number_of_votes_cast = row_count 
    print("Election Results" + "\n")
    print("_____________________________________" + "\n")
    print("Total Votes: " + str(total_number_of_votes_cast) + "\n")
    print("_____________________________________" + "\n")
    election_dictionary_keys = election_dictionary.keys()
    candidate_count = len(election_dictionary_keys)
    for rows in election_dictionary_keys:
        print(rows + ": "+ str(round(((election_dictionary.get(rows)/total_number_of_votes_cast)*100),3))+ "% " + "(" + str(election_dictionary.get(rows)) + ")" + "\n")
    print("_____________________________________" + "\n")
    print("Winner: " + popular_candidate )
    print("_____________________________________" + "\n")
   #
   # open the file to hold the analysis results in write mode
   # Write the analsysis results to the 
   #
    with open(output_path, 'w') as file:
        file.writelines("Election Results" + "\n") 
        file.writelines("_____________________________________" + "\n") 
        file.writelines("\n" + "Total Votes: " + str(total_number_of_votes_cast) + "\n")
        file.writelines("_____________________________________" + "\n") 
        for rows in election_dictionary_keys:
            file.writelines(rows + ": "+ str(round(((election_dictionary.get(rows)/total_number_of_votes_cast)*100),3))+ "% " + "(" + str(election_dictionary.get(rows)) + ")" + "\n")
        file.writelines("_____________________________________" + "\n")
        file.writelines("\n" "Winner: " + popular_candidate + "\n")
        file.writelines("_____________________________________" + "\n")

main()