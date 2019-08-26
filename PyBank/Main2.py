# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:52:35 2019

@author: jehix
"""

# This will be my phtyon PyBank Script
import os

import csv 
  
#Define Variables



# csv file name 
budgetdata_csv = os.path.join("Resources", "budget_data.csv")

# reading csv file subtrqcting one for header row
with open(budgetdata_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    Total_Months = list(csvreader)
    row_count = (len(Total_Months)-1)
    
       
    print("    Financial Analysis") 
    print("----------------------------")
    print("Total Months: " + str(row_count))
    print('Total: ' + str(total))
    print("Greatest Increase in Profits: ")
    print("Greatest Decrease in Profits: ")
    