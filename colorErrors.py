import numpy as np
import colorsys

# HELPER FUNCTIONS

def hsv(color):
	return np.array(colorsys.rgb_to_hsv(*(color / 255)))

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

@colorError
def sumHsvAbsoluteDifference(a, b):
	aHSV = hsv(a)
	bHSV = hsv(b)
	return np.sum(np.abs(aHSV - bHSV))

@colorError
def maxHsvAbsoluteDifference(a, b):
	aHSV = hsv(a)
	bHSV = hsv(b)
	return np.max(np.abs(aHSV - bHSV))