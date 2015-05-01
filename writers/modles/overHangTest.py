
import math
file = open("overHangTest.gcode", "w")

bounds = 20.0

layers = 3000.0
mSpeed = 400.0
dSpeed = 150.0
step = 1

moveSpeed = "F" + str(mSpeed * 60) + " "
drawSpeed = "F" + str(dSpeed * 60) + " "

drawSpeed2 = "F" + str(dSpeed * 60 * 2) + " "

drawSpeed4 = "F" + str(dSpeed * 60 * 4) + " "

laserOn = " E1.0"
laserOff = " "

offset = bounds/2




delays = 2

#G0 X-22.952 Y-7.842 Z0.030
#G1 X23.504 Y-9.673 E0.02758


#for layer in range(0,int(layers), step):
#	#shift = math.sqrt(layer/layers) * layers
#	shift = (layer/layers)*(layer/layers) * layers/100 
#	print int(shift) * "+"
#	file.write("G1 " + "Z" + str(layer/100.0) + " \n")
#	file.write("G1 "  + drawSpeed +"X" +str(-bounds/2 + shift) + " Y" + str(bounds/2) + laserOff + " \n")
#	file.write("G1 " + drawSpeed +"X" +str(-bounds/2 + shift) + " Y" + str(bounds) + laserOn + " \n")
#	file.write("G1 " + drawSpeed +"X" +str(0 + shift) + " Y" + str(bounds) + laserOn + " \n")



layer = 0
for layer in range(0,int(layers), step):
	#shift = math.sqrt(layer/layers) * layers
	shift2 = math.sin(layer/layers *20) * layers/10
	print int(shift2 ) * "-"
	file.write("G1 " + "Z" + str(layer/1.0) + " \n")
	file.write("G1 "  + drawSpeed +"X" +str(-bounds/2 + shift2) + " Y" + str(bounds/2) + laserOff + " \n")
	file.write("G1 " + drawSpeed +"X" +str(-bounds/2 + shift2) + " Y" + str(bounds) + laserOn + " \n")
	file.write("G1 " + drawSpeed +"X" +str(0 + shift2) + " Y" + str(bounds) + laserOn + " \n")









file.close()
