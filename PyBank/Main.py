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
    
    
    row_count = list(csvreader)
    Total_Months = (len(row_count)-1)
#  Define Variables
   
    revenue = 0
    rows=[r for r in csvreader]
# Loop throu data using range function to start as row 2
for i in range(1, len(rows)):
       revenue= int(row[1]) + revenue
       row=rows[i]
       print(revenue)
       
       
# print result
   
print("    Financial Analysis")
print("----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: " + " $ " + str(revenue))
print("Average Change:  $")
print("Greatest Increase in Profits: ")
print("Greatest Decrease in Profits: ")