import os
import csv
import json

"""
This file reads files in the training-data folder and outputs all relevant and required data to training-data.json file.
"""


data: list[list[tuple[float, float]]] = []       # each item is a list of (high, low) tuples

# get all .txt files in the training-data subdirectory
trainingDataFolder = "training-data"
try:
    urls = [os.path.join(trainingDataFolder, f) for f in os.listdir(trainingDataFolder) if os.path.isfile(os.path.join(trainingDataFolder, f)) and f.endswith(".txt")]
except FileNotFoundError:
    print("No folder training-data found. Please see README.md for more information about the dataset.")
    exit()
if len(urls) == 0:
    print("The training-data folder seems to be empty. Please see README.md for more information about the dataset.")
    exit()
print(f"Using {len(urls)} files of training data")

for url in urls:
    with open(url) as f:
        companyData = []
        lines = csv.reader(f)
        for i, line in enumerate(lines):
            if i == 0:
                continue
            companyData.append((float(line[2]), float(line[3])))       # high, low
        data.append(companyData)



def handleTenDays(days: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """ Param days is a list of (high,low) tuples in dollars. Returns the same list where first day's high is index 100. """
    hundredLevel = 0.01 * days[0][0]
    return [(day[0]/hundredLevel, day[1]/hundredLevel) for day in days]

def calculateOutcome(tenth: tuple, eleventh: tuple) -> int:
    tenAverage = (tenth[0] + tenth[1]) / 2
    elevenAverage = (eleventh[0] + eleventh[1]) / 2
    changePercent = (elevenAverage - tenAverage) / tenAverage
    if changePercent >= 0.02:
        return 0
    if changePercent >= -0.02:
        return 1
    return 2

def generateX(arr: list[tuple[float, float]]) -> list[float]:
    """ Parameter arr is a list of (high,low) tuples and the return is an one-dim list: [high, low, high, low, ...] """
    newArr = []
    for high, low in arr:
        newArr.append(high)
        newArr.append(low)
    return newArr

preparedData: list[tuple[list[float], int]] = []        # each item is a tuple: ([high,low,high,low...] list with len=20; outcome)
for company in data:
    for startIndex in range(0, len(company)-11, 11):
        elevenDays = company[startIndex:startIndex+11]
        outcome = calculateOutcome(elevenDays[9], elevenDays[10])
        preparedData.append((generateX(handleTenDays(elevenDays[:10])), outcome))

with open("training-data.json", "w") as f:
    f.write(json.dumps(preparedData))

print(f"Training set size {len(preparedData)}")
