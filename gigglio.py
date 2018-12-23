import numpy as np
import PIL.Image
import requests
from io import BytesIO
import sys
import colorErrors

def fixColor(hexColor):
	r = ((hexColor >> 16) % 256)
	g = ((hexColor >> 8) % 256)
	b = (hexColor % 256)
	return np.array((r, g, b), dtype=np.float32)

COLORS = [
	fixColor(0xffffff), # White
	fixColor(0xbfbfbf), # Gray
	fixColor(0xff0000), # Red
	fixColor(0xff6b00), # Orange
	fixColor(0xffe71f), # Yellow
	fixColor(0x00d224), # Green
	fixColor(0x00aefe), # Cyan
	fixColor(0x3a00d0), # Indigo
	fixColor(0xb500b7), # Purple
	fixColor(0xe275a7), # Pink
	fixColor(0xab5130), # Brown

	fixColor(0x000000), # Black
	fixColor(0x4d4d4d), # Dark Gray
	fixColor(0x7f000b), # Dark Red
	fixColor(0xd33100), # Dark Orange
	fixColor(0xf3a110), # Dark Yellow
	fixColor(0x00591b), # Dark Green
	fixColor(0x00539c), # Dark Cyan
	fixColor(0x1e0064), # Dark Indigo
	fixColor(0x600068), # Dark Purple
	fixColor(0xb35072), # Dark Pink
	fixColor(0x6b3214), # Dark Brown

	# fixColor(0x8e9359)
]

def closestColor(inputColor, metric):

	bestColorIndex = None
	bestColor = None
	bestError = np.inf
	for colorIndex, color in enumerate(COLORS):

		error = metric(inputColor, color)

		if error < bestError:
			bestError = error
			bestColorIndex = colorIndex
			bestColor = color

	return bestColorIndex, bestColor

def doTheThing(dif):
	# url = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/687px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg"
	# url = "https://vignette.wikia.nocookie.net/the-many-adventures-of-minecraft-rogers/images/4/44/1200x630bb.jpg/revision/latest?cb=20170512053111"
	if len(sys.argv) > 1:
		url = sys.argv[1]
	else:
		url = "https://vignette.wikia.nocookie.net/avatar/images/8/82/Fanon_Appa.png/revision/latest?cb=20130308032654&format=original"
	img = PIL.Image.open(BytesIO(requests.get(url).content))
	img.thumbnail(dif, PIL.Image.ANTIALIAS)
	# img.show()


	dataList = []
	colorIndicesList = []
	for metric in colorErrors.COLOR_ERRORS:
		data = np.array(np.asarray(img))[:,:,:3]
		colorIndices = np.zeros(data.shape[0:2], np.int32)
		for y in range(data.shape[0]):
			for x in range(data.shape[1]):
				colorIndices[y, x], data[y, x] = closestColor(data[y, x], metric)
		colorIndicesList.append(colorIndices)
		dataList.append(data)

	return colorIndicesList, dataList

if __name__=="__main__":
	colorIndicesList, dataList = doTheThing([100, 100])
	data = np.concatenate(dataList, axis=0)
	outputImg = PIL.Image.fromarray(data)
	outputImg.resize((outputImg.size[0] * 5, outputImg.size[1] * 5), PIL.Image.NEAREST).show()
