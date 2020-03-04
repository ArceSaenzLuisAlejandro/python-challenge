import os
import csv
import statistics 

# -----------------PyBank-----------------
csv_path = os.path.join("budget_data.csv")

months = 0
total_P_L = 0
average_P_L = []
date_list = []
greatest_increase = 0
date_increase = 0
greatest_decrease = 0
date_decrease = 0

with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip headers
    next(csvreader, None)
    # Headers: "Date", "Profit/Losses"
    
    for row in csvreader:
        # Months counter
        months += 1
        # Net total amount of P/L
        total_P_L = total_P_L + float(row[1])
        # List for average of P/L
        average_P_L.append(float(row[1]))
        # List for storing dates
        date_list.append(row[0])
    # Append the difference from the next row and the actual row
    average_result = []
    for i,j in enumerate(average_P_L):
        if i < len(average_P_L)-1:
            pls = average_P_L[i+1]-average_P_L[i]
            average_result.append(pls)
    # Get average from the List  
    average = statistics.mean(average_result)
    # Get index for greatest increase and decrease
    for i, j in enumerate(average_result):
        if i < len(average_result)-1:
            if average_result[i+1] > greatest_increase:
                greatest_increase = average_result[i+1]
                flag_increase = i+2
            if average_result[i+1] < greatest_decrease:
                greatest_decrease = average_result[i+1]
                flag_decrease = i+2


print("Financial Analysis" +
      "\n------------------" +
      "\nTotal Months: " + str(months) +
      "\nTotal: " + str(total_P_L) +
      "\nAverage Change: $" + str(average) +
      "\nGreates Increase in Profits: " + 
      str(date_list[flag_increase]) + " ($" + str(greatest_increase) + ")" +
      "\nGreatest Decrease in Profits: " + 
      str(date_list[flag_decrease]) + " ($" + str(greatest_decrease) + ")" 
     )

file_txt = open("Financial_Analysis.txt","w") 
write = ["Financial Analysis",
      "\n------------------",
      "\nTotal Months: ", str(months),
      "\nTotal: ", str(total_P_L),
      "\nAverage Change: $", str(average),
      "\nGreates Increase in Profits: ", 
      str(date_list[flag_increase]), " ($", str(greatest_increase),")",
      "\nGreatest Decrease in Profits: ", 
      str(date_list[flag_decrease]), " ($", str(greatest_decrease), ")",
    ]  
file_txt.writelines(write) 
file_txt.close()