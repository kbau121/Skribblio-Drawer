import numpy as np
import colorsys

# HELPER FUNCTIONS

def hsv(color):
	return np.array(colorsys.rgb_to_hsv(*(color / 255)))

# REGISTRATION SYSTEM

COLOR_ERRORS = []
COLOR_ERROR_NAMES = []

def colorError(name):
	def decorator(f):
		COLOR_ERRORS.append(f)
		COLOR_ERROR_NAMES.append(name)
		return f
	return decorator

# ERROR METRICS

@colorError("Sum Absolute Difference")
def sumAbsoluteDifference(a, b):
	return np.sum(np.abs(a - b))

@colorError("Max Absolute Difference")
def maxAbsoluteDifference(a, b):
	return np.max(np.abs(a - b))

@colorError("Sum Absolute Difference HSV")
def sumHsvAbsoluteDifference(a, b):
	aHSV = hsv(a)
	bHSV = hsv(b)
	return np.sum(np.abs(aHSV - bHSV))

@colorError("Max Absolute Difference HSV")
def maxHsvAbsoluteDifference(a, b):
	aHSV = hsv(a)
	bHSV = hsv(b)
	return np.max(np.abs(aHSV - bHSV))
