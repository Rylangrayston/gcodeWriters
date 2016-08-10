
import math
file = open("centerHist.gcode", "w")

bounds = 20.0

layers = 80.0
mSpeed = 80.0
dSpeed = 80.0
step = 1

moveSpeed = "F" + str(mSpeed * 60) + " "
drawSpeed = "F" + str(dSpeed * 60) + " "

drawSpeed2 = "F" + str(dSpeed * 60 * 2) + " "

drawSpeed4 = "F" + str(dSpeed * 60 * 4) + " "

laserOn = " E1.0"
laserOff = " "

offset = bounds/2




delays = 2

def circle(radius,resolution,posX = 0 ,posY = 0):
	code = ""
	deg = 0 
	code += "G1 " + drawSpeed +"X" +str(math.cos(math.radians(deg))* radius + posX) + " Y" + str(math.sin(math.radians(deg)) * radius + posY) + laserOff + " \n"
	#print "circle   radius: ", radius, "    resoluton: ", resolution
	for deg in range(0,360 ,360/resolution):
		code += "G1 " + drawSpeed +"X" +str( math.cos(math.radians(deg))* radius + posX ) + " Y" + str(math.sin(math.radians(deg)) * radius + posY) + laserOn + " \n"

	deg = 0
	code += "G1 " + drawSpeed +"X" +str(math.cos(math.radians(deg))* radius + posX) + " Y" + str(math.sin(math.radians(deg)) * radius + posY) + laserOn + " \n"	
	return code

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

stepOverRate = .1

stack1Pos = -20
stack3Pos = 0
stackWidth = 1
preTestLayers = 20 
noCorrectionLayers = 30

layer = 0

file.write(circle(radius = 7,resolution = 20,posX = 0 ,posY = 0))
file.write(circle(radius = 3,resolution = 20,posX = 0 ,posY = 0))
file.write(circle(radius = 1,resolution = 20,posX = 0 ,posY = 0))

for layer in range(0,int(layers), step):


	if layer < layers:
		file.write("G1 " + "Z" + str(layer/1.0) + " \n") # go up a layer
		file.write("G1 " + drawSpeed +"X" +str(0) + " Y" + str(stackWidth) + laserOff + " \n")
		file.write("G1 " + drawSpeed +"X" +str(0) + " Y" + str(0) + laserOn + " \n")

		









file.close()
