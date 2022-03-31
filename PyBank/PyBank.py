#In this challenge, you are tasked with creating a Python script to analyze the financial records of your company. 
#You will give a set of financial data called budget_data.csv. 
# The dataset is composed of two columns: "Date" and "Profit/Losses". 
# (Thankfully, your company has rather lax standards for accounting, so the records are simple.)
#Your task is to create a Python script that analyzes the records to calculate each of the following:
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

# Import lib for .csv file handling 
import csv
# Import lib for os path handling 
import os

path = os.path.join("Resources","budget_data.csv")
analysis_path = os.path.join("Analysis","BankAnalysis.txt")

# Set summary variables to default value
row_count = 0
total_change = 0 
Great_inc = 0
Great_dec = 0 

with open(path) as budget_data:
    budget = csv.reader(budget_data, delimiter=',')

    # Skip header row 
    next(budget)
        
    # Iterate through each row/line of budget_data
    for row in budget:
        # when it is the first time through print heading information
        if row_count == 0:
            total_profit = int(row[1])
            last_month = int(row[1])
            row_count += 1 # Increment row count

        else: # For all other rows add to total profit and calculate change
            # Set Current month value for readability
            current_month = int(row[1])
            total_profit += current_month
            total_change += (last_month - current_month)
            # Find the change month over month and correct the sign
            current_change = ((last_month - current_month)* -1)
            row_count += 1 # Increment row count

            # Check if this row has a greater increase then the one we are holding than update 
            if Great_inc <= current_change:
                Great_inc = current_change
                Great_inc_date = row[0]                    
            # Check if this row has a greater decrease then the one we are holding than update
            elif Great_dec >= current_change:
                Great_dec = current_change
                Great_dec_date = row[0]
            last_month = int(row[1])

# Calculate average change 
average_change = (total_change /  (row_count -1) * -1) 


# Build results list
results = ["Finacial Analysis","-" * 20,f'Total Months:  {row_count} ',
    f'Total profit: ''${:,.2f}'.format(total_profit),
    f'Average change: ''${:,.2f}'.format(round(average_change,2)),
    f'Greatest Increase in Profits: {Great_inc_date} (${Great_inc})',
    f'Greatest Decrease in Profits: {Great_dec_date} (${Great_dec})']

print('\n' .join(results))

# Write results to .txt file 
with open(analysis_path, 'w') as analysis:
    analysis.write('\n'.join(results))