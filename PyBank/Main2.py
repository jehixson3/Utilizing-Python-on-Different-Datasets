# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:52:35 2019

@author: jehix
"""
# This will be my phtyon PyBank Script
import os
import csv

# csv file name
budgetdata_csv = os.path.join("Resources", "budget_data.csv")

# reading csv file
with open(budgetdata_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
#  Define Variables
   months = 0
   profit = 0
   total_profit = 0
   profit_change = 0
   previous_profit = profit
   sum_profit_change = 0
   
# Better way to count rows always check python documentation
   rows=[r for r in csvreader]
   
# Loop through data using range function to start as row 2
for i in range(1,len(rows)):
   months=months+1
   row=rows[i]
   profit += int(row[1])
   total_profit = int(row[1]) + total_profit
   
#Find change in profit from last month to this month
profit_change = profit - previous_profit
print(profit_change)
#add change in profit to net change in profit
sum_profit_change = profit_change + sum_profit_change
print ("_________________")
print(sum_profit_change)
# set value of previous profit for next loop
previous_profit = profit

#finish calculations
average_profit_change = (sum_profit_change/(months))
    
#Print Results
print("    Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: " + " $ " + str(total_profit))
print("Average Change:  $" + str(average_profit_change))
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")