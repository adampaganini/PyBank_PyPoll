import os
import csv

budgetdata_csv = os.path.join("Resources", "budget_data.csv")
text_file = os.path.join("Analysis", "PyBank.txt")

# iterate through the rows counting all months
# output the number of months into the terminal
total_months = 0
month = []
monthly_change = []
total_change = 0
max_increase = ["", 0]
max_decrease = ["", 99999999]

with open (budgetdata_csv, "r") as data:
    reader = csv.reader(data)
    header = next(reader)
    first_row = next(reader)
    total_months += 1
    # typically, data columns will be int, but cover your bases by converting to int()
    total_change += int(first_row[1])
    previous_net = int(first_row[1])
    #[0]= month column and [1] is profit/loss column
    for row in reader:
        total_months += 1 
        total_change += int(row[1])
        net_change = int(row[1])-previous_net 
        previous_net = int(row[1])
        #take stuff and put it in an empty list I set up above:
        monthly_change += [net_change]
        month.append(row[0])# could work also for line 29

        if net_change> max_increase[1]:
            max_increase[0]=row[0]
            max_increase[1]=net_change
        if net_change < max_decrease[1]:
            max_decrease[0]=row[0]
            max_decrease[1]=net_change


# average monthly change calculation (sum)/len
avg_change = sum(monthly_change)/len(monthly_change)
#use ''' to make massive comment / string value that observes line endings
output=f'''

Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_change:,.2f}
Average Change: ${avg_change:,.2f}
Greatest Increase in Profits: {max_increase[0]} (${max_increase[1]:,.2f})
Greatest Decrease in Profits:  {max_decrease[0]} (${max_decrease[1]:,.2f})'''

print(output)

with open (text_file,"w") as outputfile:
    outputfile.write(output)


# add up all the numbers in the 2nd column
# output that sum into the terminal
# calc the difference between each profit/loss and it's adjecnt profit/loss and output to a new column
# average that column's values together
# output that average to the term
# calculate the largest number in the new column of diffs between each month
# output the largest increase number of increase
# calculate the smallest number in the new column of diffs between each month
# output the largest decrease number of increase