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
offset2 = bounds/5

delays = 2

#G0 X-22.952 Y-7.842 Z0.030
#G1 X23.504 Y-9.673 E0.02758

for layer in range(0,layers):
	file.write("G1 " + drawSpeed +"X" +str(-offset) + " Y" + str( bounds - offset) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-offset) + " Y" + str( bounds - offset+1) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(0      ) + " Y" + str( bounds) + laserOff + " \n")#----
	file.write("G1 " + drawSpeed +"X" +str( bounds) + " Y" + str( bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds) + " Y" + str(-bounds) + laserOn + " \n")

	for delay in range(0,delays):
		file.write("G1 " + drawSpeed +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
		file.write("G1 " + drawSpeed +"X" +str( -bounds) + " Y" + str(-bounds) + laserOn + " \n")

	file.write("G1 " + drawSpeed +"X" +str( -bounds) + " Y" + str(bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(0      ) + " Y" + str( bounds) + laserOn + " \n")#----



#######

	file.write("G1 " + drawSpeed2 +"X" +str(-offset) + " Y" + str( bounds - offset - offset2) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-offset) + " Y" + str( bounds - offset+1 -offset2) + laserOn + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str(0      ) + " Y" + str( bounds - offset2) + laserOff + " \n")#----
	file.write("G1 " + drawSpeed2 +"X" +str( bounds) + " Y" + str( bounds - offset2) + laserOn + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str(-bounds) + " Y" + str(-bounds) + laserOn + " \n")

	for delay in range(0,delays):
		file.write("G1 " + drawSpeed2 +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
		file.write("G1 " + drawSpeed2 +"X" +str( -bounds) + " Y" + str(-bounds) + laserOn + " \n")

	file.write("G1 " + drawSpeed2 +"X" +str( -bounds) + " Y" + str(bounds - offset2) + laserOn + " \n")
	file.write("G1 " + drawSpeed2 +"X" +str(0      ) + " Y" + str( bounds - offset2) + laserOn + " \n")#----


#######

	file.write("G1 " + drawSpeed4 +"X" +str(-offset) + " Y" + str( bounds - offset - offset2*2) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-offset) + " Y" + str( bounds - offset+1 - offset2*2) + laserOn + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str(0      ) + " Y" + str( bounds - offset2*2) + laserOff + " \n")#----
	file.write("G1 " + drawSpeed4 +"X" +str( bounds) + " Y" + str( bounds - offset2*2) + laserOn + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str(-bounds) + " Y" + str(-bounds) + laserOn + " \n")

	for delay in range(0,delays):
		file.write("G1 " + drawSpeed4 +"X" +str( bounds) + " Y" + str(-bounds) + laserOn + " \n")
		file.write("G1 " + drawSpeed4 +"X" +str( -bounds) + " Y" + str(-bounds) + laserOn + " \n")

	file.write("G1 " + drawSpeed4 +"X" +str( -bounds) + " Y" + str(bounds - offset2*2) + laserOn + " \n")
	file.write("G1 " + drawSpeed4 +"X" +str(0      ) + " Y" + str( bounds - offset2*2) + laserOn + " \n")#----

file.close()
