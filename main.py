import os
import csv

with open('budget_data.csv', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#Counter for monthly total
        

#Variables
    count = 0
    revenue_sum = 0
    max_loss = 0
    loss_date = "unknown"
    gain = "unknown"
    avg = 0
    revenue_current = 0
    prev_month_rev = 0
    delta = 0
    for row in csvreader:
        count = count + 1
        revenue_current = revenue_current + int(row[1])
        
#The net total amount of "Profit/Losses" over the entire period
loss_date.append(row[0])
profit.append(row[1])
revenue_sum = revenue_sum + int(row[1])

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
monthly_change = int(row[1]) - prev_month_rev
prev_month_rev = int(row[1])
avg = monthly_change / count

#The greatest increase in profits (date and amount) over the entire period
maxprofit = max(monthly_change)
maxdate = date[monthly_change.index(maxprofit)]

#The greatest decrease in losses (date and amount) over the entire period
max_loss = min(monthly_change)
max_lossdate = date[monthly_change.index(max_loss)
]
#Create monthly change list
monthly_change.append(monthly_change)

print ("Financial Analysis")
print("Total Months": + str(count))
print("Total": + str(revenue_sum))
print("Average Change": + str(avg))
print("Greatest Increase in Profits": (maxprofit)
print("Greatest Decrease in Profits": (max_loss))

print(output)




