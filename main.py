#need to determine the total number of months
#net profit/losses over the entire period
#average in profit loss over the period
#greatest increase in profit (date and amount) over the period
#greatest decrease in profit (date and amount) over the period

#imports the os module- allowing us to create file paths
import os
#the module we will use to read the CSV
import csv

print("inside"+ os.getcwd())
total=0
totalmonths=0
monthly_difference=[]
date=[]
revenue=[]

with open("/Users/kassyedwards/Documents/Analytics Course/PythonHWCSV.csv", newline="" ) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

#header row exclusion
    csv_header = next(csvreader)
    print(f"csv_header: {csv_header}")
#for loop for total, total months, and revenue
    for row in csvreader:
        total= total + int(row[1])
        totalmonths=totalmonths + 1

        revenue.append(int(row[1]))
#for loop for the mathematical functions
    for i in range(1,len(revenue)):
        monthly_difference.append(revenue[i]-revenue[i-1])
        average_difference=round((sum(monthly_difference))/(len(monthly_difference)),2)
        greatest_increase=max(monthly_difference)
        greatest_decrease=min(monthly_difference)
#print statements
    print(f"Net Profit = $", total)
    print(f"totalmonths =", totalmonths)
    print(f"$",average_difference)
    print('Maximum is: $', greatest_increase)
    print('Minimum is: $', greatest_decrease)


# Financial Analysis
  # ----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)
