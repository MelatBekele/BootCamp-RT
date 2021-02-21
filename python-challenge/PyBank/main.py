import os
import csv 
import collections

# Path to collect data from the Resources folder
budget_data_path = os.path.join('..', 'pyBank','Resources', 'budget_data.csv')
#file = '../pyBank/Resources/budget_data.csv'

lines = 0 
total = 0 
previous = 0 
list2 = []
highdate  = 0
highpriof = 0
lowdate = 0
lowpriof = 0

with open(budget_data_path, 'r') as budget_data_file:
    budget_data = csv.reader(budget_data_file, delimiter=",")
    budget_header = next(budget_data)
    fisrt = budget_data_file.readline()
    profitfirst = int(fisrt.split(',', 1) [1])
     
    for budget_header in budget_data:
        lines = lines + 1 #number of rows
        total = total + int(budget_header[1])  #total for profit 

        #change in profit (profit1 - profit2)/total row
        change = previous - int(budget_header[1])
        previous = int(budget_header[1]) 
        list2.append(change)

        sumof_change = sum(list2)/lines
        
        #Greatest increase and decrease
         
        if highpriof < int(budget_header[1]):
            highdate = str(budget_header[0])
            highpriof = int(budget_header[1])

       
        if lowpriof > int(budget_header[1]):
            lowdate = str(budget_header[0])
            lowpriof = int (budget_header[1])

result = (f"Financial Analysis \n " f"----------------------------\n"
f"Total Months: {lines} \n"
f"Total: $ {total}\n"
f"Average  Change: $ {sumof_change}\n"
f"Greatest Increase in Profits: {highdate} ($ {highpriof})\n"
f"Greatest Decrease in Profits: {lowdate} ($ {lowpriof})\n")

print (result)

output_path = os.path.join('..', 'pyBank','Resources',"new.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w',newline='')as csvfile:
    csvfile.write(result)

