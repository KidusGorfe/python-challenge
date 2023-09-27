# Specify the file path
file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv"

# Read data from the CSV file
with open(file_path, 'r') as file:
    lines = file.readlines()

# Remove the header line
header = lines.pop(0)

# Initialize variables to store financial analysis data
total_months = 0
total_profit_losses = 0
previous_profit_loss = None
total_change = 0
greatest_increase = None
greatest_decrease = None
greatest_increase_date = None
greatest_decrease_date = None

# Process the data
for line in lines:
    date, profit_loss = line.strip().split(',')
    profit_loss = int(profit_loss)
   
    # Count months and calculate total profit/losses
    total_months += 1
    total_profit_losses += profit_loss
   
    # Calculate the change and update the total change
    if previous_profit_loss is not None:
        monthly_change = profit_loss - previous_profit_loss
        total_change += monthly_change
   
    # Update greatest increase and decrease
    if greatest_increase is None or profit_loss > greatest_increase:
        greatest_increase = profit_loss
        greatest_increase_date = date
    if greatest_decrease is None or profit_loss < greatest_decrease:
        greatest_decrease = profit_loss
        greatest_decrease_date = date
   
    previous_profit_loss = profit_loss

# Calculate the average change
average_change = total_change / (total_months - 1)

# Prepare the financial analysis summary
header = """Financial Analysis
----------------------------"""
total_months_summary = f"Total Months: {total_months}"
total_summary = f"Total: ${total_profit_losses}"
average_change_summary = f"Average Change: ${average_change:.2f}"
greatest_increase_summary = f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})"
greatest_decrease_summary = f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})"

# Print the financial analysis summary to the console
print(header)
print(total_months_summary)
print(total_summary)
print(average_change_summary)
print(greatest_increase_summary)
print(greatest_decrease_summary)

# Specify the file path for exporting results
output_file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\analysis\\PyBankOutput.txt"

# Export the financial analysis summary to a text file
with open(output_file_path, "w") as file:
    file.write(header + "\n")
    file.write(total_months_summary + "\n")
    file.write(total_summary + "\n")
    file.write(average_change_summary + "\n")
    file.write(greatest_increase_summary + "\n")
    file.write(greatest_decrease_summary + "\n")

# Print a message indicating where the results were exported
print("Financial analysis results exported to", output_file_path)
