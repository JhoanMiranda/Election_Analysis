#Add dependencies.
import csv
import os

#Assing a variable to load a file from a path
file_to_load = os.path.join("Resources","election_results.csv")  

#Create a filename variable to save the file to the path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election resoults and read the file 
with open(file_to_load) as election_data:

    #.Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    
    #Print the header row.
    headers = next(file_reader) 
    print(headers)
    
        


#Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")

# Write three counties to the file.
    

# Close the file
outfile.close()