import pandas as pd
from itertools import combinations

print("Hello WOrld")
totoResultsHistory = pd.read_csv("toto_results.csv")

def ExtractWinningNumbers(totoResultsData):
    winningNumbersList = []

    i = 0
    while i < totoResultsData.shape[0]:
    #while i <= 3:
        winningNumber = []
        for n in range(2, 9):
            winningNumber.append(totoResultsData.loc[i].iat[n])
        winningNumbersList.append(set(winningNumber))
        i += 1

    return winningNumbersList

def CountWinningNumberMatches(winningNumbersData, inputNumbers):
    i = 0
    for winningNumbers in winningNumbersData:
        if inputNumbers.issubset(winningNumbers):
            i += 1
    
    return i

def CheckWinningNumberMatch(winningNumber, inputNumber):
    failMatchCount = 0
    for i in range(0, len(inputNumber)):
        for j in range(0, len(winningNumber)):
            print(str(inputNumber[i]) + ": " + str(winningNumber[j]))
            if inputNumber[i] != winningNumber[j]:
                failMatchCount += 1
            else:
                break
        if failMatchCount > 1:
            break

    return failMatchCount <= 1

# If winning number of 7 were to be split into 6 combinations, how many would match in the history of winning numbers?
def CountMatchesForCombinationsInHistory(winningNumbersData, amountToMatchFilter=7):
    print("Matches in history more than " + str(amountToMatchFilter) + " times: ")
    allMatchesSet = set()
    for number in winningNumbersData:
        combinationsOfNumber = list(combinations(number, 6))
        count = 0

        for combinationNumber in combinationsOfNumber:
            count += CountWinningNumberMatches(winningNumbersData, set(combinationNumber))

        if count > amountToMatchFilter: 
            sortedNumber = sorted(number)
            print(str(sortedNumber) + ": " + str(count))
            allMatchesSet.update(set(sortedNumber))
    print("")
    print("Collated numbers: " + str(allMatchesSet))
    noMatchSet = set()
    i = 1
    for x in allMatchesSet:
        while(x != i):
            noMatchSet.add(i)
            i += 1
        i += 1
    print("")
    print("Remaining numbers: " + str(noMatchSet))
    print("")

# If you bought more than 6 numbers (ie System 7 and above), how many would've matched in history?
def CountMatchesForCombinations(winningNumbersData, inputNumber):
    print("Number of Matches for " + str(inputNumber))
    combinationsOfNumber = list(combinations(inputNumber, 6))

    for combinationNumber in combinationsOfNumber:
        count = CountWinningNumberMatches(winningNumbersData, set(combinationNumber))
        print(str(sorted(combinationNumber)) + ": " + str(count))
    print("")


winningNumbers = ExtractWinningNumbers(totoResultsHistory)

# MENU
choice = 'W'
while (choice != 'L'):
    # Menu Options
    print("Options")
    print("1. Search matches")
    print("2. View repeated winning draws in history")
    print("L. to exit")
    choice = input("Input: ")

    match choice:
        case '1':
            # Input
            inputString = input("Enter your numbers (separated by space): ")
            inputString = inputString.split(' ')

            # Convert to int set for subset comparison
            numbersToMatch = set()
            for number in inputString:
                numbersToMatch.add(int(number))
            
            # Search count
            count = CountWinningNumberMatches(winningNumbers, numbersToMatch)
            print("Number of Matches: " + str(count))
            print()
            CountMatchesForCombinationsInHistory(winningNumbers)
            CountMatchesForCombinations(winningNumbers, numbersToMatch)
        
        case 'L':
            print("Goodbye.")
        case _:
            print("Please enter a valid input.")