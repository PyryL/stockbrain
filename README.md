# StockBrain
This project is related to a computer science course [Building AI](https://buildingai.elementsofai.com/) at Helsinki University.

⚠️ **Warning!** The user of this model is responsible of all financial loss oneself. This is just an experimental project.

## Summary

1. Let me introduce **StockBrain**: a machine learning model that predicts the direction of a stock market based on ten previous days.
2. Knowing where the stocks are going is an important skill for investors - both professionals and individuals - because it's the way they make money. This AI model helps with this problem by giving an idea of what is maybe going to happen next day, so that the user can find the best time to buy and sell shares.
3. Some CC0 public domain licensed data was used to train this model. The original data set can be found [here](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs). The set contains about 690 MB of historical data about stock markets. In order to limit the number of input parameters, only the high and low data was being used to train the neural network.
4. My model is most likely being used on investor's desktop by themself or by their automatised investing AI. It's important to make sure that the user understands the limits and weaknesses of this model. This should only be used as an extra advice.
5. The phenomenon that this AI is built to model (stock market movement) is not always predictable and regular. Unexpected events - such as COVID-19 in March 2020 - may occur. The investors are always responsible of their money themselves.
6. The AI could become better by taking account of more parameters and key values as well as longer-term changes in the stock price. The whole project could grow and reach attention by proving its capability in action.
7. Dependencies can be found later in this Readme. The idea of this project is my own and all of the code (excluding dependencies) is written solely by me without forking etc.


## TL;DR - How can I use it?

Make sure that you have installed all of the required dependencies listed below. Also check your Python's version. Then run the `ui.py` file.


## About the code

### Dependencies

Below is a table showing the libraries on which this project is directly depending. Please note that these libraries also have their own dependencies.

<table>
<tr>
<th>Name</th>
<th>License</th>
<th>Tested with version</th>
</tr>
<tr>
<td><a href="https://github.com/joblib/joblib">joblib</a></td>
<td>BSD 3-Clause</td>
<td>1.1.0</td>
</tr>
<tr>
<td><a href="https://github.com/scikit-learn/scikit-learn">sklearn</a></td>
<td>BSD 3-Clause</td>
<td>1.0.1</td>
</tr>
<tr>
<td><a href="https://github.com/ranaroussi/yfinance">yfinance</a>*</td>
<td>Apache License 2.0</td>
<td>0.1.68</td>
</tr>
</table>

\*Yfinance offers an extra feature that allows user to input stock's symbol (e.g. "AAPL") instead of the price history manually. This makes the program much easier to use, but installation of this library is optional.

This project requires Python 3.7 or higher (built and tested on 3.9.9). Following libraries are being used from the standard library: os, random, csv, json.

### Training data
As mentioned, CC0 licensed [dataset](https://www.kaggle.com/borismarjanovic/price-volume-data-for-all-us-stocks-etfs) was used to thain this model. The dataset is so big that I decided not to include the data in this reposity. If you need the dataset (e.g. to train the model further), place the `Stocks` folder of the dataset into same folder with all of the python files of this reposity, and rename it to `training-data`.

### Building the model

To read more about the process of making the AI model, see [about-model.md](about-model.md).