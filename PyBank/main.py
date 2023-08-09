
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
   #
   # Defining the key variables required for the analysis
   #
   total_number_of_months = 0
   net_profit_losses = 0
   rowcounter = 0
   Previous_month_profit_loss = 0
   total_profit_losses_change = 0
   changes_in_profit_losses_month = 0
   average_profit_loss = 0
   greatest_increase_in_profits = 0
   greatest_increase_date = ""
   greatest_decrease_in_profits = 0
   greatest_decrease_date = ""
   date_list = []
   profit_losses_list = []
   # 
   # Defining the path to the source data file to be analyzed
   #       
   csvpath = os.path.join("..","PyBank\Resources", "budget_data.csv")
   #
   # Define the file where the result of the analysis will be stored
   #
   output_path = os.path.join("..","PyBank\Analysis", "Pybank Assignment Result.txt")

   with open(csvpath) as csvfile:
         # CSV reader specifies delimiter and variable that holds contents
         csvreader = csv.reader(csvfile, delimiter=',')
         # print(csvreader)
         #
         # Read the header row first (skip this step if there is no header)
         csv_header = next(csvreader)
         # print(csv_header)
         #        
         # Read each row of data after the header
         #
         for row in csvreader:
             rowcounter = rowcounter + 1
             #print(row)
             date_list.append(row[0])
             #Picking the first column of each row holding the date information
             datesection = row[0]
             #print(datesection[0:3])
             #Calculating the change in profit/loss for the current row with the previous one
             changes_in_profit_losses_month = int(row[1]) - Previous_month_profit_loss
             # Test to see if the change is bigger than the previous biggest change recorded
             if changes_in_profit_losses_month > greatest_increase_in_profits:
                   greatest_increase_in_profits = changes_in_profit_losses_month
                   greatest_increase_date = datesection

            #Test to see if the change is smaller than the previous greatest loss change recorded
             if changes_in_profit_losses_month < greatest_decrease_in_profits:
                   greatest_decrease_in_profits = changes_in_profit_losses_month
                   greatest_decrease_date = datesection
             #
             # Calculate the total changes in profit and losses
             total_profit_losses_change = total_profit_losses_change + changes_in_profit_losses_month
             #
             # Check if the data is for the start of the year
             #if datesection[0:3] == "Jan":
             #  year_start_profit_loss = int(row[1])
                        
             profit_losses_list.append(row[1])
             net_profit_losses = net_profit_losses + int(row[1])
             #Previous_date_month = row[0]
             Previous_month_profit_loss = int(row[1])
   # Generate and print the summary information from the data        
   total_number_of_months = len(date_list)
   average_profit_loss = round(total_profit_losses_change / total_number_of_months,2)
   print("Finanical Analysis")
   print("_____________________________________")
   print("Total Months: " + str(total_number_of_months))
   print("Total:  $" +str(net_profit_losses))
   print("Average Change: $", str(average_profit_loss))
   print("Greatest Increase in Profits: ", greatest_increase_date, " ($",str(greatest_increase_in_profits),")" )
   print("Greatest Decrease in Profits: ", greatest_decrease_date, " ($",str(greatest_decrease_in_profits),")" )
   #
   # open the file and write ther results
   #
   with open(output_path, 'w') as file:
      file.writelines("Finanical Analysis" + "\n") 
      file.writelines("_____________________________________" + "\n") 
      file.writelines("Total Months: " + str(total_number_of_months) + "\n")
      file.writelines("Total:  $" + str(net_profit_losses) + "\n")
      file.writelines("Average Change: $" + str(average_profit_loss) + "\n")
      file.writelines("Greatest Increase in Profits: " + greatest_increase_date + " ($" + str(greatest_increase_in_profits) + ")" + "\n" )
      file.writelines("Greatest Decrease in Profits: " + greatest_decrease_date + " ($" + str(greatest_decrease_in_profits) + ")" + "\n" )
main()


    





