file = open("/home/rylangrayston/git/tkpeachyprinter/src/test-gcode.gcode", "w")

bounds = 20

layers = 100
mSpeed = 400
dSpeed = 100

moveSpeed = "F" + str(mSpeed * 60) + " "
drawSpeed = "F" + str(dSpeed * 60) + " "

drawSpeed2 = "F" + str(dSpeed * 60 * 2) + " "

drawSpeed4 = "F" + str(dSpeed * 60 * 4) + " "

laserOn = " E1.0"
laserOff = " "

offset = bounds/7


delays = 2

#G0 X-22.952 Y-7.842 Z0.030
#G1 X23.504 Y-9.673 E0.02758

for layer in range(0,layers):
	file.write("G1 " + drawSpeed +"X" +str(-bounds) + " Y" + str(0) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds + offset) + " Y" + str(bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds + offset) + " Y" + str(0) + laserOn + " \n")

	file.write("G1 " + drawSpeed +"X" +str(bounds - offset) + " Y" + str(-bounds) + laserOff + " \n") # move to other triangle
	
	file.write("G1 " + drawSpeed +"X" +str(bounds - offset) + " Y" + str(bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(bounds) + " Y" + str(0) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(bounds - offset) + " Y" + str(-bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(bounds - offset) + " Y" + str(0) + laserOn + " \n")#

	file.write("G1 " + drawSpeed +"X" +str(-bounds + offset) + " Y" + str(0) + laserOff + " \n")








file.close()
