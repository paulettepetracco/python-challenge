import os
import csv

#Store filepath in a variable
budget_one = os.path.join("r'/Users/paulettepetracco/Bootcamp_Code_Challenges/python-challenge/PyBank/Resources/budget_data.csv")
save_path = "/Users/paulettepetracco/Bootcamp_Code_Challenges/GH_Repositories/python-challenge/PyBank"
completeName = os.path.join(save_path, "output.txt")

# Variables
number_months = 0
total = 0
profits = []
losses = []
total_profits = 0
total_losses = 0
average_change = 0
greatest_increase = []
greatest_decrease= []


#pull from the csv file
with open(r'/Users/paulettepetracco/Bootcamp_Code_Challenges/python-challenge/PyBank/Resources/budget_data.csv', newline = '') as csvfile:
    budget_one = csv.reader(csvfile)
    
    # find the total number of months with loop
    for row in budget_one:
        
        #The total number of months included in the dataset
        if row[0]=="Date":continue
        number_months += 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])
        
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        if int(row[1]) >= 0: profits.append(row)
        else: losses.append(row)
        
    # The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for profit in profits:
        total_profits = total_profits + int(profit[1])
        if len(greatest_increase) == 0: greatest_increase = profit
        if len(greatest_increase) and int(profit[1]) > int(greatest_increase[1]): greatest_increase = profit
    
    for loss in losses:
        total_losses = total_losses + int(loss[1])
        if len(greatest_decrease) == 0: greatest_decrease = loss
        if len(greatest_decrease) and int(loss[1]) < int(greatest_decrease[1]): greatest_decrease = loss
        
    
    average_change = (total_profits + total_losses) / number_months
    
# print financial analysis 
print("Financial Analysis", file=open(completeName,"a"))   
print("----------------------------", file=open(completeName,"a"))    
print(f"Total Months: {number_months}", file=open(completeName,"a"))
print(f"Total: ${total}", file=open(completeName,"a"))
print(f"Average Change {average_change}", file=open(completeName,"a"))
print(f"Greatest_Increase: $({greatest_increase[1]})", file=open(completeName,"a"))
print(f"Greatest_Decrease: $({greatest_decrease[1]})", file=open(completeName,"a"))