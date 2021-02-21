import os
import csv 
import collections

# Path to collect data from the Resources folder
PYpoll = os.path.join('..', 'Pypoll','Resources', 'election_data.csv')
#file = '../pyBank/Resources/budget_data.csv'
lines = 0 
candidate_names = []
NameDic = {}
total_votes = 0
total = []
combine = ""
with open(PYpoll, 'r') as py_file:
    py_data = csv.reader(py_file, delimiter=",")
    py_header = next(py_data)
    for py_header in py_data:
      lines = lines + 1 
      if py_header[2] not in candidate_names:
            candidate_names.append(py_header[2])
            NameDic[py_header[2]] = 0
            NameDic[py_header[2]] += 1

result = (f"Election Results \n " f"----------------------------\n" f"Total Votes: {lines} \n" 
f"----------------------------\n" f"{candidate_names}")

print (result)

output_path = os.path.join('..',  'Pypoll','Resources',"new.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w',newline='')as csvfile:
    csvfile.write(result)