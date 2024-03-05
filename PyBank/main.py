import os
import csv

#Path to collect data from the Resources folder
budget_csv = os.path.join('Resources', 'budget_data.csv')

#Path for the output file
output_path = os.path.join("analysis","Analysis.csv")

#Iterate in file from resource folder
with open(budget_csv, 'r') as csvfile:
    #Initialize variables
    count_month = 1
    profit_losses_val=[]
    profit_losses_dat=[]
    mean_pro_lo=0

    #Read the file
    csvreader=csv.reader(csvfile,delimiter=',')
    #Skip the file headers
    header=next(csvreader)
    #Get the first value since it will be used later on
    first_value=next(csvreader)
    pre_value=int(first_value[1])
    total_profit=int(first_value[1])

    for row in csvreader:
        #Calculate Total Profit (Total)
        total_profit+=int(row[1])

        #Calculate sum of change so we can calculate the average later
        profit_losses_val.append(int(row[1])-pre_value)
        profit_losses_dat.append(row[0])
        pre_value=int(row[1])
        mean_pro_lo+=profit_losses_val[count_month-1]

        #Calculate Total Months
        count_month += 1

    #Find greatest increase
    great_in = profit_losses_val[0]
    for i in profit_losses_val:
        if i > great_in:
            great_in = i
    index_in=profit_losses_val.index(great_in)

    #Find greatest decrease
    great_de = profit_losses_val[0]
    for i in profit_losses_val:
        if i < great_de:
            great_de = i
    index_de=profit_losses_val.index(great_de)

    #Calculate the change average
    mean_pro_lo=mean_pro_lo/(count_month-1)
    #This line was taken from URL
    #https://www.javatpoint.com/how-to-get-2-decimal-places-in-python
    mean_pro_lo=format(mean_pro_lo,".2f")

#Print in the terminal
print(f"""Financial Analysis
----------------------------
Total Months: {count_month}""")
print(f"Total: ${total_profit}")
print(f"Average Change ${mean_pro_lo}")
print(f"Greatest Increase in Profits: {profit_losses_dat[index_in]} (${great_in})")
print(f"Greatest Decrease in Profits: {profit_losses_dat[index_de]} (${great_de})")

#Print in an output file
with open(output_path,'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {count_month}"])
    csvwriter.writerow([f"Total: ${total_profit}"])
    csvwriter.writerow([f"Average Change ${mean_pro_lo}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {profit_losses_dat[index_in]} (${great_in})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {profit_losses_dat[index_de]} (${great_de})"])