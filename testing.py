import joblib
import json
from random import choice
from sklearn.neural_network import MLPClassifier


"""
This file runs a sequence of random tests with the AI model.
"""

print("Loading AI model")
modelFileName = "model.sav"
model: MLPClassifier = joblib.load(modelFileName)


print("Loading test dataset")
try:
    with open("training-data.json") as f:
        data = json.loads(f.read())
except FileNotFoundError:
    print("File training-data.json not found. Please run prepare-data.py first.")
    exit()


print("Testing")
# raising, middle, falling
corrects = [0, 0, 0]
incorrects = [0, 0, 0]

testCount = 1000
for i in range(testCount):
    company: list = choice(data)
    tenDays = company[0]
    predictedOutcome = model.predict([tenDays])[0]
    correctOutcome = company[1]
    if predictedOutcome == correctOutcome:
        corrects[correctOutcome] += 1
    else:
        incorrects[correctOutcome] += 1


print()
print(f"Ratio {sum(corrects)}/{testCount} = {sum(corrects)/testCount*100:.2f}%")
print(f"Correct predictions: {corrects}")
print(f"Incorrect predictions: {incorrects}")
