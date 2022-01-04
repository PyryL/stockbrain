# About the code and the model

This file contains more information about how the model was built.



## Files' abstracts

* **prepare-data.py** is being used to read files in the training-data folder and output only relevant and required data to training-data.json file. You need to run this file only if you change the contents of the training-data folder.
* **train.py** creates an AI model out from the data in training-data.json file. The model is being tested right away with a small set of data and then it's being saved into a .sav file. You need to run this file after changing the contents of training-data.json, and after changing the layer configuration (the `layerConfig` variable in the code).
* **testing.py** runs a sequence of random tests with the AI model. You can control the workflow with `testCount` variable. After having multiple different models created with train.py, change the `modelFileName` variable to change between them. Execution of this file is never required, but it can be run whenever wanted.
* **yahooapi.py** provides an interface to easily access the price history of a specific stock by the symbol (e.g. "AAPL"). This file is not meant to be run itself but to be imported to other files.
* **ui.py** is used to use the AI model in action. The user can interact with the model via CLI.



## Working with layer configuration

The neural network consists of layers and each of them has a number of nodes. Because the model uses last 10 days' high and low price, there are 20 input nodes. Since the model classifyes the stock price into three categories (rising, middle, dropping), there are 3 output nodes. But in between of input and output, there are unknown number of hidden layers, for which I had to come up with an optimal number of nodes. Below is a table showing the results of tests with different configurations.

<table>
<tr>
<th>Hidden layers</th>
<th>Accuracy</th>
</tr>
<tr>
<td>(16, 5)</td>
<td>77.4%</td>
</tr>
<tr>
<td>(12, 10)</td>
<td>77.8%</td>
</tr>
<tr>
<td>(11)</td>
<td>77.8%</td>
</tr>
<tr>
<td>(15)</td>
<td>77.7%</td>
</tr>
<tr>
<td>(5)</td>
<td>77.3%</td>
</tr>
<tr>
<td>(15, 10, 5)</td>
<td>77.8%</td>
</tr>
<tr>
<td>(17, 13, 10, 6)</td>
<td>77.9%</td>
</tr>
<tr>
<td>(17, 14, 12, 9, 6)</td>
<td>77.9%</td>
</tr>
</table>

More intense comparsion with three testing rounds between some of the best configurations gave following results:
<table>
<tr>
<th>Layers</th>
<th colspan="3">Accuracy</th>
<th>Average</th>
</tr>
<tr>
<td>(11)</td>
<td>78.30%</td>
<td>77.20%</td>
<td>76.50%</td>
<td>≈77.33%</td>
</td>
</tr>
<tr>
<td>(12, 10)</td>
<td>76.90%</td>
<td>77.80%</td>
<td>77.90%</td>
<td>≈77.53%</td>
</td>
</tr>
<tr>
<td>(15, 10, 5)</td>
<td>75.60%</td>
<td>80.10%</td>
<td>75.80%</td>
<td>≈77.17%</td>
</td>
</tr>
<tr>
<td>(17, 13, 10, 6)</td>
<td>76.10%</td>
<td>77.20%</td>
<td>76.20%</td>
<td>76.50%</td>
</td>
</tr>
<tr>
<td>(17, 14, 12, 9, 6)</td>
<td>72.30%</td>
<td>79.10%</td>
<td>77.70%</td>
<td>≈76.37%</td>
</td>
</tr>
</table>

Relying on these results, I chose `(12, 10)` to be the layer configuration of the final model.