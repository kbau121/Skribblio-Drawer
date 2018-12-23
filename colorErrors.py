import numpy as np


# REGISTRATION SYSTEM

COLOR_ERRORS = []

def colorError(f):
	COLOR_ERRORS.append(f)
	return f


# ERROR METRICS

@colorError
def sumAbsoluteDifference(a, b):
	return np.sum(np.abs(a - b))

@colorError
def maxAbsoluteDifference(a, b):
	return np.max(np.abs(a - b))
