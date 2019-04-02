#imports the os module- allowing us to create file paths
import os
#the module we will use to read the CSV
import csv

print("inside"+ os.getcwd())
Total = 0
candidates = ['Khan', 'Correy', 'Li', 'O’Tolley']
Khan=0
Correy=0
Li=0
OTolley=0
percent_won_Khan = 0
percent_won_Correy=0
percent_won_Li =0
percent_won_OTolley =0


total_votes=[]

#open csv file
with open("/Users/kassyedwards/Documents/election_data.csv", newline="" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    for row in csvreader:
        Total = (Total +1)
        #count (candidates[Khan])
        if row[2]==candidates[0]:
            Khan= Khan+1
            percent_won_Khan = (int(Khan)/Total)*100
        #count candidates Correy
        if row[2]==candidates[1]:
            Correy=Correy+1
            percent_won_Correy = (int(Correy)/Total)*100
        #count canddiates Li
        if row[2]==candidates[2]:
            Li=Li+1
            percent_won_Li = (int(Li)/Total)*100
        #count candidates OTolley
        if row[2]==candidates[3]:
            OTolley=OTolley+1
            percent_won_OTolley = (int(OTolley)/Total)*100

    print(f"the total number of votes cast =", Total)
    print(f"The candidates were", candidates)
    print(f"Khan recieved ", Khan, "votes and", percent_won_Khan, "% of the total votes")
    print(f"Correy recieved", Correy, "votes and", percent_won_Correy, "% of the total votes")
    print(f"Li recieved", Li, "votes and", percent_won_Li, "% of the total votes" )
    print(f"OTolley recieved", OTolley, "votes and", percent_won_OTolley, "% of the total votes")
















#mylist = list(dict.fromkeys(mylist))




    # Iterate over the original list and for each element
    # add it to uniqueList, if its not already there.
#for row in csvreader:
    #if row not in uniquelist:
            #uniqueList.append(row)
    #print(uniqueList)
    # Return the list of unique elements




#The total number of votes cast
#A complete list of candidates who received votes [Candidates]
#The percentage of votes each candidate won [percent_won]
#The total number of votes each candidate won [total_votes]
#The winner of the election based on popular vote.[winner]
