import pynput
import time
from pynput.mouse import Button, Controller

import gigglio

mouse = Controller()

pos = [483, 217]
dif = [102, 76]		# Resolution

brushSize = [1138, 864]
moveAmount = 8

#XChange = 813
#YChange = 610

color = [[585, 850], [610, 850], [635, 850], [660, 850], [685, 850], [710, 850], [735, 850], [760, 850], [785, 850], [810, 850], [835, 850], [585, 875], [610, 875], [635, 875], [660, 875], [685, 875], [710, 875], [735, 875], [760, 875], [785, 875], [810, 875], [835, 875]]
currColor = 0

white = [585, 850]
lightGray = [610, 850]
lightRed = [635, 850]
lightOrange = [660, 850]
lightYellow = [685, 850]
lightGreen = [710, 850]
lightCyan = [735, 850]
lightBlue = [760, 850]
lightPurple = [785, 850]
lightPink = [810, 850]
lightBrown = [835, 850]
black = [585, 875]
darkGray = [610, 875]
darkRed = [635, 875]
darkOrange = [660, 875]
darkYellow = [685, 875]
darkGreen = [710, 875]
darkCyan = [735, 875]
darkBlue = [760, 875]
darkPurple = [785, 875]
darkPink = [810, 875]
darkBrown = [835, 875]

def nextColor():
	global currColor
	global color

	currColor += 1
	if(currColor >= len(color)):
		currColor = 0

def clickAt(clickPos):
	global Button
	global tempPos
	global mouse

	tempPos = mouse.position
	mouse.position = clickPos
	mouse.click(Button.left, 1)
	mouse.position = tempPos

thing, otherThing = gigglio.doTheThing(dif)

mouse.position = (pos[0], pos[1])
# for y in range(dif[1]):
# 	for x in range(dif[0]):
for y in range(thing.shape[0]):
	for x in range(thing.shape[1]):
		time.sleep(0.007)
		mouse.move(moveAmount, 0)
		mouse.click(Button.left, 1)

		# nextColor()
		clickAt(color[thing[y, x]])

	mouse.position = (pos[0], pos[1] + moveAmount)
	pos[1] += moveAmount