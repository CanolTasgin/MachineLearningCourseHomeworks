# -*- coding: utf-8 -*-
"""CS412_HW1_ccanol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IBTv4iUdQ0ewk1w7tDzff9cmETFrCRgy
"""

import pandas as pd

mydata = pd.read_table("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", sep=",")
mydata.columns = ['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Output']

print(mydata)

print(mydata.shape)

print(mydata.columns)

print(mydata.head(10))

print(mydata.sample(n=10))

print(mydata.tail(10))

print(mydata.iloc[99])