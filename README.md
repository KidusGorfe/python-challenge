# python-challenge

Tutor Help: 
Met with a Tutor who encouraged me to make this section of my code dynamic:

#Winner Announcement 
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

Originally my code was just a print statement that printed out that Diana was the winner of the election 

ChatGPT export: 

Utilized ChatGPT to give me the structure for exporting my code in this section: 

outputFilePath = file_path = "C:\\Users\\kidus\\OneDrive\\Documents\\GitHub\\python-challenge\\PyPoll\\analysis\\PyPollOutput"

with open(outputFilePath, "w") as file:
    for result in results:
        file.write(result + "\n")

print("Results exported to", outputFilePath)

