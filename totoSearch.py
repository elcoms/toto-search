import numpy as np
import pandas as pd

print("Hello WOrld")
totoResultsHistory = pd.read_csv("toto_results.csv")

def ExtractWinningNumbers(totoResultsData):
    sortedWinningNumbers = []

    i=0
    while i < totoResultsData.shape[0]:
    #while i <= 3:
        winningNumbersList = []
        for n in range(2, 9):
            winningNumbersList.append(totoResultsData.loc[i].iat[n])
        sortedWinningNumbers.append(sorted(winningNumbersList))
        i += 1

    return sortedWinningNumbers

def CountWinningNumberMatches(winningNumbersData, inputNumbers):
    i = 0
    for winningNumbers in winningNumbersData:
        if np.array_equal(winningNumbers, inputNumbers):
            i += 1
    
    return i


winningNumbers = ExtractWinningNumbers(totoResultsHistory)
numbersToMatch = [2, 9, 10, 43, 45, 46, 13]
count = CountWinningNumberMatches(winningNumbers, sorted(numbersToMatch))
print("Number of Matches: " + str(count))