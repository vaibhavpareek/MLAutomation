#!/usr/bin/env python
#i have created this small program for the testing and as it is using random function so our program will be tested fine
import numpy as np
y_test = np.array([1, 0, 0, 1, 0])
y_pred = np.random.random((5))
def acc(y_true, y_pred):
    return np.equal(y_true, np.round(y_pred)).mean()
print(str(int(acc(y_test, y_pred)*100)))