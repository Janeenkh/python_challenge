import csv
import os 

file_to_open = os.path.join("Resources", "budget_data.csv")
with open(file_to_open) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")

    header = next(csvreader)
    print(header)

    count = 0
    total = 0
    great_inc = 0
    great_dec = 0

    for row in csvreader:
        count = count + 1
        total = total + float(row[1])
    
    count_result = (f"Total month:{count}\n"
                    f"Total:{total}\n")
    print(count_result)

with open(file_to_open) as datafile:
    csvreader = csv.reader(datafile, delimiter=",")    
    header = next(csvreader)  
    firstrow = next(csvreader)  

    firstmonth=float(firstrow[1])
    prevrow=firstmonth
    totalchange= 0
    counter = 1

    for row in csvreader:
        change = float(row[1]) - prevrow
        prevrow= float(row[1])
        totalchange = totalchange + change
        avgchange = totalchange/(count-1)

        if change > great_inc:
            great_inc = change
            great_month = row[0]

        if change < great_dec:
            great_dec = change
            low_month = row[0]

    change_result = (f"Average change: {avgchange}\n"
    f"Greatest Increase in Profit: {great_month} and ${great_inc}\n"
    f"Greatest Decrease in Profit: {low_month} and ${great_dec}")
    print(change_result)

file_to_save = os.path.join("analysis", "result.txt")
with open(file_to_save, "w") as txtfile:
    txtfile.write(count_result)
    txtfile.write(change_result)





