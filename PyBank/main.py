import os
import csv

 # Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:

    count_month = 0
    total_profit = 0

    csvreader=csv.reader(csvfile,delimiter=',')
    header=next(csvreader)
    
    for row in csvreader:
        count_month += 1
        total_profit+=int(row[1])


print(f"""Financial Analysis
----------------------------
Total Months: {count_month}""")
print(f"Total: {total_profit}")
