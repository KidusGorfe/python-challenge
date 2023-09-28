# Specify the file path
file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\Resources\\PyPoll.csv"

# Initialize variables
voteCount = 0
TVcharlie, TVdiana, TVray = 0, 0, 0

# Open CSV file and count votes
with open(file_path, 'r') as file:
    lines = file.readlines()
    header_row = lines[0]  # Assuming the first line contains the header
    lines = lines[1:]  # Remove the header line
    
    for line in lines:
        voteCount += 1
        parts = line.strip().split(',')  # Split the line by commas

        # Assuming the structure is Ballot ID, County, Candidate
        ballot_id, county, candidate_name = parts

        if candidate_name == "Charles Casper Stockham":
            TVcharlie += 1
        elif candidate_name == "Diana DeGette":
            TVdiana += 1
        elif candidate_name == "Raymon Anthony Doane":
            TVray += 1

# Header
header = """Election Results
----------------------------"""
print(header)

# Total Votes
votes = f"Total Votes: {voteCount}"
print(votes)

# Spacer
spacer1 = "----------------------------"
print(spacer1)

# Count of Votes and Percentages for Charlie
PCTcharlie = "{:.3f}".format((TVcharlie / voteCount) * 100)
fincharlie = f"Charles Casper Stockham: {PCTcharlie}% ({TVcharlie})"
print(fincharlie)

# Count of Votes and Percentages for Diana
PCTdiana = "{:.3f}".format((TVdiana / voteCount) * 100)
findiana = f"Diana DeGette: {PCTdiana}% ({TVdiana})"
print(findiana)

# Count of Votes and Percentages for Ray
PCTray = "{:.3f}".format((TVray / voteCount) * 100)
finray = f"Raymon Anthony Doane: {PCTray}% ({TVray})"
print(finray)

# Spacer
spacer2 = "----------------------------"
print(spacer2)

# Winner Announcement
if TVcharlie > TVdiana and TVcharlie > TVray:
    winner = "Winner: Charles Casper Stockham"
elif TVdiana > TVray:
    winner = "Winner: Diana DeGette"
else:
    winner = "Winner: Raymon Anthony Doane"

print(winner)

# Spacer
spacer3 = "----------------------------"
print(spacer3)

# Exporting File
results = [header, votes, spacer1, fincharlie, findiana, finray, spacer2, winner, spacer3]

outputFilePath = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\analysis\\PyPollOutput"

with open(outputFilePath, "w") as file:
    for result in results:
        file.write(result + "\n")

print("Results exported to", outputFilePath)
