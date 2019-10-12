#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('com.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values

from sklearn.cross_validation import train_test_split
X_train, X_test, Y_train, y_test = train_test_split(x,y, test_size = 0.2, random_state=0)
