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

# reading csv file subtrqcting one for header row
with open(budgetdata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#  Define Variables
    months = 0 
    revenue = 0
    revenue_change = 0
# Better way to count rows always check python documentation
    rows=[r for r in csvreader]
    
# Loop throu data using range function to start as row 2
for i in range(1,len(rows)):
    months=months+1
    row+=rows[1]
    revenue= int(row[1]) + revenue
    
# Calcuate change in revenue
    
    
# possibly do other things with data/rows 
    print("    Financial Analysis") 
    print("----------------------------")
    print("Total Months: " + str(months))
    print("Total: " + " $ " + str(revenue))
#  print("Average Change  $" + int(change_revenue))
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
   
 

        
       
              