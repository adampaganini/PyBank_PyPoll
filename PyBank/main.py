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
    for row in reader:
        total_months += 1 
        total_change += int(row[1])
        net_change = int(row[1])-previous_net 
        previous_net = int(row[1])
        monthly_change += [net_change]
        month.append(row[0])# could work also for line 29

        if net_change> max_increase:
            max_increase[0]=row[0]
            max_increase[1]=net_change
# average monthly change calculation (sum)/len

output=f'''
Financial Analysis
----------------------------
Total Months: {total_months}
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)'''

print(output)
with open()


# add up all the numbers in the 2nd column
# output that sum into the terminal
# calc the difference between each profit/loss and it's adjecnt profit/loss and output to a new column
# average that column's values together
# output that average to the term
# calculate the largest number in the new column of diffs between each month
# output the largest increase number of increase
# calculate the smallest number in the new column of diffs between each month
# output the largest decrease number of increase