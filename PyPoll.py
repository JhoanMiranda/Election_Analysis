#Add dependencies.
import csv
import os
#from sqlite3 import Row

#Assing a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")  

#Create a filename variable to save the file to the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#variable that start from 0
total_votes = 0
# list of candidates 
candidate_options = []

#votes to each candidate
candidate_votes = {}

#Wining candidate and Wining count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election resoults and read the file 
with open(file_to_load) as election_data:

    #.Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
     #Print the header row.
    headers = next(file_reader) 
    
     #print each row in the csv file.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #print candidate name for each row
        candidate_name = row[2]

        #If candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #Begin tracking candidate's  vote count        
            candidate_votes[candidate_name] = 0
        #+ each vote
        candidate_votes[candidate_name] += 1


    #loop to get percentage  
    for candidate_name in candidate_votes:
        #retreive vote count on candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

    
        #Print total Votes.
        print(f"({candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


        #Determine winning Vote count and candidate

        #Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #If true then set winning count = votes and winning count = vote_percentage

            winning_count = votes

            winning_percentage = vote_percentage
        
            #set the winning_candidate equeal to the candidate's name
            winning_candidate = candidate_name

winning_candidate_summary = (
    f"-----------------------\n"
    f"winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")


print(winning_candidate_summary)


#---------------------------------------------------    
        
#Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Write three counties to the file.
    

# Close the file
outfile.close()