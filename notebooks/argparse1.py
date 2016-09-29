#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--predict", type=float)
args = parser.parse_args()
import sklearn.linear_model
import numpy
lr = sklearn.linear_model.LinearRegression()
lr.coef_ = numpy.array([2.0])
lr.intercept_ = 0.0
print lr.predict([[args.predict]])
