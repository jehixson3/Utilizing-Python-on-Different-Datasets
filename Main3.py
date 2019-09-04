# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 14:11:16 2019

@author: jehix
"""
# This will be my python PyBank Script using Shauns video
import os
import csv

# csv file name
budgetdata_csv = os.path.join("Resources", "budget_data.csv")

#  Define Variables
months = 0
profit = 0
total_profit = 0
previous_profit = profit
average_profit_change = 0
max_profit = 0
min_profit = 99999999999
total_profit_change = 0

# Make a list to capture monthly change in profit
profit_change = []
   
# Reading csv file
with open(budgetdata_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
# Skip the header row first 
   next(csvreader, None)
  
# Read through each row of data after the header
   for row in csvreader:
       months=months+1
       profit = int(row[1])
       total_profit = profit + total_profit
         
# Calcualte changes in monthly profit
       monthly_profit_change = profit - previous_profit
       previous_profit = profit
        
# Add changes to list
       profit_change.append(monthly_profit_change)
     
# Calculate the average change in revenue
       total_profit_change = sum(profit_change)
       average_profit_change = round(total_profit_change/months, 2)

# Find the greatest increase in profits
       if (monthly_profit_change > max_profit):
          max_profit_month = row[0]
          max_profit = monthly_profit_change 
# Find the greatest decrease in profits
       if (monthly_profit_change < min_profit):
          min_profit_month = row[0]
          min_profit = monthly_profit_change 
       
# Print Results
print("    Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: " + " $" + str(total_profit))
print("Average Change:  $" + str(average_profit_change))
print("Greatest Increase in Profits: " + str(max_profit_month) + "  ($" + str(max_profit) + ")")
print("Greatest Decrease in Profits: " + str(min_profit_month) + "  ($" + str(min_profit) + ")")
 
# save summary to txt
with open('results.txt', 'w+') as file:
    #Write results to file and close file 
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months: " + str(months)+ '\n')
    file.write("Total Profit: $" + str(total_profit)+ '\n')
    file.write("Average Change: $" + str(average_profit_change)+ '\n')
    file.write("Greatest Increase in Profit: " + str(max_profit_month) + " ($"+str(max_profit)+")\n")
    file.write("Greatest Decrease in Profit: " + str(min_profit_month) + " ($"+str(min_profit)+")\n")
    file.write("----------------------------\n")
    file.close()