import json
from random import randint
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import joblib
import os

"""
This file creates an AI model out from the data in training-data.json file.
The model is being tested right away with a small set of data and then it's being saved into a .sav file.
"""


print("Preparing data sets")
try:
    with open("training-data.json") as f:
        data = json.loads(f.read())
except FileNotFoundError:
    print("The training-data.json file is missing. Please run prepare-data.py first.")
    exit()

train_x, test_x, train_y, test_y = train_test_split([a[0] for a in data], [a[1] for a in data], train_size=10000/len(data), test_size=0.2)


print(f"Training with {len(train_x)} training sets")
layerConfig = (15, 10)
model = MLPClassifier(hidden_layer_sizes=layerConfig)
model.fit(train_x, train_y)
score = model.score(test_x, test_y)
print(f"Model accuracy was {score*100:.1f}%")


# generate a random filename for the new model so it does not overwrite existing models
outputFileName = f"output-{randint(10000, 99999)}.sav"
joblib.dump(model, outputFileName)
print(f"Model saved to file {outputFileName}")


# on macOS, this plays a nice little sound when running the script finishes
os.system("afplay /System/Library/Sounds/Submarine.aiff")
