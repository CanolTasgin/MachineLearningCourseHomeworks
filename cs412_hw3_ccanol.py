# -*- coding: utf-8 -*-
"""CS412_HW3_ccanol.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15qxt_DeMFYjN163ka0rzhRwERWBiBFcB

#CS412 Homework 3
Celal Canol Taşgın - 20761
ccanol@sabanciuniv.edu

Read data with pandas and put column names

#DOWNLOADED DATASET AND CHECKED THE VALUES
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.metrics import accuracy_score, f1_score, classification_report
import matplotlib.pyplot as plt

url="https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
mydata = pd.read_csv(url,names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'FlowerType']) 
df = pd.DataFrame(mydata)

data = df[['SepalLength',	'SepalWidth',	'PetalLength',	'PetalWidth']]
target = df['FlowerType']

feature_names = [name.replace("(cm)", "").strip() for name in data]
target_names = target

X = data
y = target
dataset = pd.DataFrame(X, columns=feature_names)

dataset['target'] = y
dataset.head()

target_names

df.head()

df.shape

df.info()

# Commented out IPython magic to ensure Python compatibility.
import seaborn as sns
# %matplotlib inline
import matplotlib.pyplot as plt
iris = datasets.load_iris()
X = iris.data
y = iris.target
sns.set(font_scale=1.5)
sns.pairplot(df,hue="FlowerType",height=3);
plt.show()

X

from sklearn import preprocessing

X = preprocessing.normalize(X)
X

from sklearn.model_selection import train_test_split

X_full_train, X_test, y_full_train, y_test = train_test_split(X, y, random_state=3, test_size=0.2)

print("Full training data size: %d\nTest data size: %d" % (len(X_full_train), len(X_test)))

X_full_train.shape, X_test.shape

y_test

"""Split Data"""

## Validation / Development

X_train, X_valid, y_train, y_valid = train_test_split(X_full_train, y_full_train, random_state=0, test_size=0.25)
## Split size 0.25 to retrieve (60-20)-20

print("Training data size: %d\nValidation data size: %d" % (len(X_train), len(X_valid)))

"""#DECISION TREE"""

#from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier

#Default parameters
#dt_model = DecisionTreeClassifier(criterion='gini', max_depth=None, min_samples_split=2, min_samples_leaf=1)

"""TRIED THESE VALUES AS MAXIMUM DEPTH AND LOOKED FOR THE BEST & WORST TREES"""

max_depth_values = [50, 20, 15, 10, 5, 3]

f1_scores = []
dt_models = []
for param_value in max_depth_values:
    dt_model = DecisionTreeClassifier(criterion='entropy', max_depth=param_value, min_samples_split=2, min_samples_leaf=1)
    dt_model.fit(X_train, y_train)

    y_pred = dt_model.predict(X_valid)

    acc = accuracy_score(y_valid, y_pred)
    f1 = f1_score(y_valid, y_pred, average='macro')

    f1_scores.append(f1)
    dt_models.append(dt_model)
    print("Validation results, Decision Tree with max_depth %s:\tAccuracy: %%%.2f\tF1 Score: %%%.2f" % (str(param_value), acc*100, f1*100))

worst_index = np.argmin(f1_scores)
best_index = np.argmax(f1_scores)
best_max_depth_param = max_depth_values[best_index]
worst_max_depth_param = max_depth_values[worst_index]
best_model = dt_models[best_index]
worst_model = dt_models[worst_index]
print("\nBest results is achieved with max_depth=%s" % str(best_max_depth_param))
print("\nWorst results is achieved with max_depth=%s" % str(worst_max_depth_param))

from sklearn.tree import plot_tree

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (5,5), dpi=200)

tree_plot = plot_tree(dt_model,
            feature_names = feature_names, 
            class_names=target_names,
            filled = True)

"""Defined Gini Function

Tried to create a gini function below which takes parameters in dataset such as sepal widht,length etc.
"""

#Gini Function
#a, b and c are the quantities of each class (setosa, versicolor, virginica)
def gini(a,b,c,d):
    a1 = (a/(a+b+c+d))**4
    b1 = (b/(a+b+c+d))**4
    c1 = (c/(a+b+c+d))**4
    d1 = (d/(a+b+c+d))**4
    return 1 - (a1 + b1 + c1 + d1)

"""Read rows of the dataset and assigned it to seperate lists"""

sLength_list = []
sWidth_list = []
pLength_list = []
pWidth_list = []
gini_list = []
setosa_prob_list.append(b)
setosaAmount, virginicaAmount, versicolorAmount = 0,0,0
for index, rows in dataset.iterrows(): 
  sLength_list.append(rows.SepalLength)
  sWidth_list.append(rows.SepalWidth)
  pLength_list.append(rows.PetalLength)
  pWidth_list.append(rows.PetalWidth)
  a = gini (rows.SepalLength, rows.SepalWidth, rows.PetalLength, rows.PetalWidth)
  gini_list.append(a)
  if rows.target == 'Iris-setosa':
    setosaAmount += 1
  elif rows.target == 'Iris-virginica':
    virginicaAmount += 1
  else:
    versicolorAmount += 1

print(setosaAmount,virginicaAmount,versicolorAmount)
print(gini_list)

"""I've seen that Gini scores are pretty high with this dataset and my gini function."""

#Dataframe of amount of blue, red, Probability of blue, and gini score
df = pd.DataFrame({"SepalLength": sLength_list, "SepalWidth": sWidth_list, "PetalLength": pLength_list, "PetalWidth": pWidth_list, "Gini Score": gini_list})
df = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Gini Score']]
df

"""Entropy

Tried to write entropy function and calculated entropy for each row
"""

from math import log as log

def entropy(base,a,b,c,d):
    try:
        var =  abs(((a)/(a+b+c+d)) * log(((a)/(a+b+c+d)),base)) - (((b)/(a+b+c+d)) * log(((b)/(a+b+c+d)),base)) -(((c)/(a+b+c+d)) * log(((c)/(a+b+c+d)),base)) - (((d)/(a+b+c+d)) * log(((d)/(a+b+c+d)),base))
        return var
    except (ValueError):
        return 0

#Blank lists
sLength_list = []
sWidth_list = []
pLength_list = []
pWidth_list = []
ent_list = []
setosa_prob_list = []

#Loop with log base 2
for index, rows in dataset.iterrows(): 
    a = entropy(4,rows.SepalLength, rows.SepalWidth, rows.PetalLength, rows.PetalWidth)
    b = setosaAmount/(setosaAmount+virginicaAmount+versicolorAmount)
    ent_list.append(a)
    sLength_list.append(rows.SepalLength)
    sWidth_list.append(rows.SepalWidth)
    pLength_list.append(rows.PetalLength)
    pWidth_list.append(rows.PetalWidth)
    setosa_prob_list.append(b)

df = pd.DataFrame({"SepalLength": sLength_list, "SepalWidth": sWidth_list, "PetalLength": pLength_list, "PetalWidth": pWidth_list, "Entropy": ent_list})
df = df[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Entropy']]
df

"""Worked with best model i've found before. then checked it accuracy and f1 score."""

best_model.fit(X_full_train, y_full_train)

y_pred = best_model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='macro')

print("Test results:\tAccuracy: %%%.2f\tF1 Score: %%%.2f" % (acc*100, f1*100))

worst_model.fit(X_full_train, y_full_train)

y_pred = worst_model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average='weighted')

print("Test results:\tAccuracy: %%%.2f\tF1 Score: %%%.2f" % (acc*100, f1*100))

"""I can see the difference between accuracy and F1 scores of best and worst model. Since this dataset isn't such a big one, the difference is not huge but scores of worst model is lower."""