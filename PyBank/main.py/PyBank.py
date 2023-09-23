import pandas as pd 

#Load in files 
file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\Resources\\budget_data.csv"

df = pd.read_csv(file_path)

#Header

header = print("""Financial Analysis
----------------------------""")

#Find Month Count 
monthCount = df["Date"].value_counts().sum()

print(f"Total Months: {monthCount}")

#Find Total Income
Total = df["Profit/Losses"].sum()

print( f"Total: ${Total}")

#Find Average Change

i = 0 
j = 1
count = 0
PL = "Profit/Losses"
collumnCount = df[PL].count()
change_sum = 0

while j < collumnCount:
    n = df.at[i,PL]
    n1 = df.at[j,PL]
    change = n1 - n 
    change_sum += change
    i = i+ 1
    j = j+1

averageChange = "{:.2f}".format(change_sum/(monthCount-1))

print(f"Average Change: ${averageChange}")

#Calculating and Printin Max Loss and Gain Along With Corresponding Month
df["Monthly Change"] = df[PL].diff()

maxGain = int(df["Monthly Change"].max())
maxLoss = int(df["Monthly Change"].min())
maxGainRow = df["Monthly Change"].idxmax()
maxLossRow = df["Monthly Change"].idxmin()
maxGainDate = df.loc[maxGainRow,"Date"]
maxLossDate = df.loc[maxLossRow,"Date"]

print(f"Greatest Increase in Profits: {maxGainDate} ${maxGain}")

print(f"Greatest Decrease in Profits: {maxLossDate} ${maxLoss}")

#Prepping Variables for Results Array
header = """Financial Analysis
----------------------------"""
months = f"Total Months: {monthCount}"
total = f"Total: ${Total}"
averageProfit = f"Average Change: ${averageChange}"
greatestIncrease = f"Greatest Increase in Profits: {maxGainDate} ${maxGain}"
greatestDecrease = f"Greatest Decrease in Profits: {maxLossDate} ${maxLoss}"

#Exporting File
results = [header,months, total, averageProfit, greatestIncrease, greatestDecrease]

outputFilePath = file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyBank\\analysis\\PyBankOutput"

with open(outputFilePath, "w") as file:
    for result in results:
        file.write(result + "\n")

print("Results exported to", outputFilePath)






