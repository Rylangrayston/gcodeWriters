file = open("test-gcode.gcode", "w")

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

offset = bounds/3

#G0 X-22.952 Y-7.842 Z0.030
#G1 X23.504 Y-9.673 E0.02758

for layer in range(0,layers):



	file.write("G0 " + drawSpeed +"X" +str( bounds) + " Y" + str(bounds/2 - offset) + " Z" + str(.1) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str( bounds) + " Y" + str(bounds/3 - offset) + laserOn + " \n")
	file.write("G0 " + drawSpeed +"X" +str(-bounds) + " Y" + str(bounds/2 - offset) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds) + " Y" + str(bounds/3 - offset) + laserOn + " \n")

	file.write("G0 " + moveSpeed +"X" +str( bounds) + " Y" + str(bounds/2) + " Z" + str(.1) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str( bounds) + " Y" + str(bounds/3) + laserOn + " \n")
	file.write("G0 " + moveSpeed +"X" +str(-bounds) + " Y" + str(bounds/2)+ laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds) + " Y" + str(bounds/3) + laserOn + " \n")

	file.write("G0 " + moveSpeed +"X" +str( bounds) + " Y" + str(bounds/2 + offset) + " Z" + str(.1) + laserOff + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str( bounds) + " Y" + str(bounds/3 + offset) + laserOn + " \n")
	file.write("G0 " + moveSpeed +"X" +str(-bounds) + " Y" + str(bounds/2 + offset) + laserOn + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str(-bounds) + " Y" + str(bounds/3 + offset) + laserOn + " \n")

	file.write("G0 " + moveSpeed +"X" +str( bounds) + " Y" + str(bounds/2 + offset * 2) + " Z" + str(.1) + laserOff + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str( bounds) + " Y" + str(bounds/3 + offset *  2) + laserOn + " \n")
	file.write("G0 " + moveSpeed +"X" +str(-bounds) + " Y" + str(bounds/2 + offset * 2) + laserOn + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str(-bounds) + " Y" + str(bounds/3 + offset * 2) + laserOn + " \n")







file.close()
