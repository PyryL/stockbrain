import joblib
from sklearn.neural_network import MLPClassifier
from yahooapi import YahooAPI

"""
This file is used to use the AI model in action. The user can interact with the model via CLI.
"""


class Predictor:
    def __init__(self) -> None:
        self.__model: MLPClassifier = joblib.load("model.sav")

    def __applyHundredIndexing(self, tenDays: list) -> list:
        """ Param tenDays is a list with length 20: [high, low, high, low, ...] in dollars """
        hundredLevel = 0.01 * tenDays[0]
        return [day/hundredLevel for day in tenDays]
    
    def predict(self, tenDays: list) -> int:
        return self.__model.predict([self.__applyHundredIndexing(tenDays)])[0]


class UserInterface:
    def __init__(self) -> None:
        self.__predictor = Predictor()
        self.__yahooApi = YahooAPI()
        self.__mainLoop()
    
    def __outputPrediction(self, prediction: int):
        if prediction == 0:
            print("Predicting over 2% increase tomorrow")
        elif prediction == 1:
            print("No big movements coming, less than 2% up or down")
        elif prediction == 2:
            print("Expecting more than 2% decrease tomorrow")
    
    def __tventyNumbersInput(self, cmd: str):
        nums = []
        for item in cmd.split():
            try:
                nums.append(float(item))
            except ValueError:
                print(f"Expected number, got \"{item}\" instead")
                return
        prediction = self.__predictor.predict(nums)
        self.__outputPrediction(prediction)
    
    def __symbolInput(self, cmd: str):
        highLowList = self.__yahooApi.getHighLowData(cmd)
        if highLowList == None:
            # an error occured
            return
        prediction = self.__predictor.predict(highLowList)
        self.__outputPrediction(prediction)

    def __fileInput(self, cmd: str):
        try:
            with open(cmd) as f:
                nums = [float(a.strip()) for a in f.read().split("\n")]
            if len(nums) != 20:
                raise TypeError(len(nums))
            prediction = self.__predictor.predict(nums)
            self.__outputPrediction(prediction)
        except FileNotFoundError:
            print(f"No such file named \"{cmd}\" found")
        except ValueError as e:
            print(f"Every line should contain a number, got \"{e.args[0]}\" instead")
        except TypeError as e:
            print(f"File should contain 20 lines, got {e.args[0]} instead")

    def __mainLoop(self):
        print("Please give a file name (e.g. \"test.txt\"), capitalized symbol (e.g. \"AAPL\"), 20 numbers separated with spaces or empty to exit")
        while True:
            cmd = input("-> ")
            if cmd == "":
                break
            elif len(cmd.split()) == 20:
                self.__tventyNumbersInput(cmd)
            elif cmd.isupper():
                self.__symbolInput(cmd)
            else:
                self.__fileInput(cmd)
            print()


UserInterface()
