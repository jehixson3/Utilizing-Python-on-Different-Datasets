# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:11:16 2019

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
profit_change = 0
previous_profit = profit
net_profit_change = 0
average_profit_change = 0
   
# reading csv file
with open(budgetdata_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")
   
   # Read the header row first 
   csv_header = next(csvfile)
   print(f"Header: {csv_header}")
  
    # Read through each row of data after the header
   for row in csvreader:
       months=months+1
       profit = int(row[1])
       total_profit = int(row[1]) + total_profit
   
#Find change in profit from last month to this month
       profit_change = profit - previous_profit
       print(profit_change)
       
#add change in profit to net change in profit
       net_profit_change = profit_change + net_profit_change
       print ("_________________")
       print(net_profit_change)
       
#set value of previous profit for next loop
       previous_profit = profit

#finish calculations
average_profit_change = (net_profit_change/(months))
    
#Print Results
print("    Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total: " + " $ " + str(total_profit))
print("Average Change:  $" + str(average_profit_change))
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")
 