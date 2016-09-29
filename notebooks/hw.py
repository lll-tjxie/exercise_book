#!/usr/bin/env python

import sklearn
import sklearn.linear_model
import pickle
lr = pickle.loads(open('lr.pickle').read())
print lr.predict([[2]])
