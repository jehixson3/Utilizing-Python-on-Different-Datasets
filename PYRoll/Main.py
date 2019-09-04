# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 09:52:35 2019

@author: jehix
"""

# This will be my phtyon PyPoll Script
import os
import csv

# csv file name
election_csv = os.path.join("Resources", "election_data.csv")

# Create dictionary hold candidate name and vote count.
candidate_vote_count = {}

# Set variables 
total_votes = 0
percent_vote = 0

# Reading csv file
with open(election_csv, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=",")

# skips header line
   next(csvreader, None)

# create dictionary using column 3 which has the vote data, using each name only once.
# count votes for each candidate as entries
# add 1 to vote counter for total votes 
   for row in csvreader:
       total_votes += 1
       if row[2] in candidate_vote_count.keys():
           candidate_vote_count[row[2]] = candidate_vote_count[row[2]] + 1
       else:
           candidate_vote_count[row[2]] = 1
            
#print(candidate_vote_count)
#print(str(total_votes))

# create empty lists for candidates and vote count
candidates = []
number_votes = []

# takes dictionary keys and values and puts them into lists to append
for key, value in candidate_vote_count.items():
    candidates.append(key)
    number_votes.append(value)
#print(str(candidates) + str(number_votes))

# create voter percent by number of votes
voter_percent = []
for v in number_votes:
    voter_percent.append(round((v/total_votes*100), 3))
#print(str(percent_vote))

# Find the winning candidate
winner = max(number_votes)
index = number_votes.index(winner)
winning_candidate = candidates[index]

# Print results
print("Election Result")
print("---------------------")
print("Total Votes:" + str(total_votes)+ "")
print("---------------------")
# zips candidates, vote_percent and votes into tuple
rearrange_data = zip(candidates, voter_percent, number_votes,)
#loop through and print tuple
for row in rearrange_data:
    print(row[0] + ":", str(row[1]) + "%", "(" + str(row[2]) + ")")
print("---------------------")
print("Winner : " + str(winning_candidate)) 
print("---------------------")

# Save results to file
with open('Election_Results.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("---------------------------------------\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("---------------------------------------\n")
    for i in range(len(set(candidates))):
        text.write(candidates[i] + ": " + str(voter_percent[i]) +"% (" + str(number_votes[i]) + ")\n")
    text.write("---------------------------------------\n")
    text.write("Winner : " + str(winning_candidate) + "\n")
    text.write("---------------------------------------\n")
