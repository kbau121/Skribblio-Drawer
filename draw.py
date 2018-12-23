import pynput
import time
from pynput.mouse import Button, Controller

import gigglio

mouse = Controller()

pos = [483, 217]
dif = [102, 76]		# Resolution

brushSize = [1087, 864]
moveAmount = 8

#XChange = 813
#YChange = 610

color = [[585, 850], [610, 850], [635, 850], [660, 850], [685, 850], [710, 850], [735, 850], [760, 850], [785, 850], [810, 850], [835, 850], [585, 875], [610, 875], [635, 875], [660, 875], [685, 875], [710, 875], [735, 875], [760, 875], [785, 875], [810, 875], [835, 875]]

def clickAt(clickPos):
	global Button
	global tempPos
	global mouse

	tempPos = mouse.position
	mouse.position = clickPos
	mouse.click(Button.left, 1)
	mouse.position = tempPos

thing, otherThing = gigglio.doTheThing(dif)

clickAt(brushSize)
time.sleep(0.01)

mouse.position = (pos[0], pos[1])
# for y in range(dif[1]):
# 	for x in range(dif[0]):
for y in range(thing.shape[0]):
	x = 0
	drawing = False
	while x < thing.shape[1]:

		# time.sleep(0.007)

		if not drawing:
			time.sleep(0.01)
			clickAt(color[thing[y, x]])

		mouse.move(moveAmount, 0)
		if not drawing:
			mouse.press(Button.left)
			drawing = True
			time.sleep(0.005)

		if drawing and (x == thing.shape[1] - 1 or thing[y, x] != thing[y, x + 1]):
			time.sleep(0.02)
			mouse.release(Button.left)
			drawing = False

		x += 1

	mouse.position = (pos[0], pos[1] + moveAmount)
	pos[1] += moveAmount