import numpy as np
import pandas as pd

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

winningNumbers = ExtractWinningNumbers(totoResultsHistory)
numbersToMatch = {2, 9, 10, 43, 45, 46}
count = CountWinningNumberMatches(winningNumbers, numbersToMatch)
print("Number of Matches: " + str(count))