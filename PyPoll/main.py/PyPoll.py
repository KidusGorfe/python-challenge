import pandas as pd

#Load in files 
file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\PyPoll.csv"

df = pd.read_csv(file_path)

#Header

header = """Election Results
----------------------------"""

print(header)

#Find Total Vote Count
voteCount = df["Ballot ID"].value_counts().sum()

votes = f"Total Votes: {voteCount}"

print(votes)

#Spacer

spacer1 = "----------------------------"
print(spacer1)

#Count of Votes and Percentages for Charlie

charlie = df["Candidate"] == "Charles Casper Stockham"

TVcharlie = charlie.sum()
PCTcharlie = "{:.3f}".format((TVcharlie/voteCount)*100)

fincharlie =  f"Charles Casper Stockham: {PCTcharlie}% ({TVcharlie})"

print(fincharlie)

#Count of Votes and Percentages for Diana

diana = df["Candidate"] == "Diana DeGette"

TVdiana = diana.sum()
PCTdiana = "{:.3f}".format((TVdiana/voteCount)*100)

findiana =  f"Diana DeGette: {PCTdiana}% ({TVdiana})"

print(findiana)

#Count of Votes and Percentages for Ray

ray = df["Candidate"] == "Raymon Anthony Doane"

TVray = ray.sum()
PCTray = "{:.3f}".format((TVray/voteCount)*100)

finray =  f"Raymon Anthony Doane: {PCTray}% ({TVray})"

print(finray)

#Spacer

spacer2 = "----------------------------"
print(spacer2)

#Winner Announcment 
if TVcharlie > TVdiana:
    if TVcharlie > TVray:
        winner = "Winner: Charles Casper Stockham"
    else:
        winner = "Winner: Raymon Anthony Doane"
else: 
    if TVdiana > TVray:
        winner = "Winner: Diana DeGette"
    else:
        winner = "Winner: Raymon Anthony Doane"

print(winner)
#Spacer

spacer3 = "----------------------------"
print(spacer3)

#Exporting File
results = [header, votes, spacer1, fincharlie, findiana, finray, spacer2, winner, spacer3]

outputFilePath = file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\analysis\\PyPollOutput"

with open(outputFilePath, "w") as file:
    for result in results:
        file.write(result + "\n")

print("Results exported to", outputFilePath)