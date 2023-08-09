
import os
import csv 
  
# Author: Foluke Daramola
#  This python will create the PyBank Script which will print:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The changes in "Profit/Losses" over the entire period, and then the average of those changes
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in profits (date and amount) over the entire period



def main():
    total_number_of_months = 0
    net_profit_losses = 0
    year_start_profit_loss = 0
    year_end_profit_loss =0
    Profit_loss_year = 0
    years = 0
    changes_in_profit_losses_year = 0
    average_profit_loss = 0
    greatest_increase_in_profits = 0
    greatest_decrease_in_profits = 0
    date_list = []
    profit_losses_list = []
         
    csvpath = os.path.join("..","PyBank\Resources", "budget_data.csv")

    with open(csvpath) as csvfile:
         # CSV reader specifies delimiter and variable that holds contents
         csvreader = csv.reader(csvfile, delimiter=',')
         print(csvreader)
         
         # Read the header row first (skip this step if there is no header)
         csv_header = next(csvreader)

         
        
    # Read each row of data after the header
         print(csv_header)
         for row in csvreader:
             #print(row)
             date_list.append(row[0])
             #Testing for the start of a year
             datesection = row[0]
             print(datesection[0:3])
             if datesection[0:3] == "Jan":
                year_start_profit_loss = int(row[1])

             if datesection[0:3] == "Dec":
                year_end_profit_loss = int(row[1])
                changes_in_profit_losses_year = int(year_end_profit_loss - year_start_profit_loss)
                print("year ", str(datesection[4:6])," " , str(changes_in_profit_losses_year))
             profit_losses_list.append(row[1])
             net_profit_losses = net_profit_losses + int(row[1])
             #print(date_list)
             #print(profit_losses_list)
              #year_start_profit_loss = 0
    #year_end_profit_loss =0
    #Profit_loss_year = 0
    #years = 0
   # changes_in_profit_losses_year = 0
    #average_profit_loss = 0
    #greatest_increase_in_profits = 0
    #greatest_decrease_in_profits = 0
    
    total_number_of_months = len(date_list)
    print("Total no of months = " + str(total_number_of_months))
    print("Net Total/Losses = " +str(net_profit_losses))
    

    
main()


    





