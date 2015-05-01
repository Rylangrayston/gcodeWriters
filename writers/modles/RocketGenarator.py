#This code is a first go at defineing a rocket with just math such that the math ouputs G code directly. 
#It may seem like a hard way to modle a rocket but honistly it only took a few hours and its my first try, so im going to say it was rather easy.
#Ive modled rockets in blender and openS cad before but there are many problems with both those methods, mostly to get things into gcode you have 
#to deal with a slicers interpentation of your modle. Im suspitons that rounding errors, or other artifacts from mesh data, are making for low quality prints 
#in the peachy printer. Getting precice control of the gcode will help me figur out the culprates. 
#also this little script pumps out a 10000 layer rocket in about 1 second flat, thats way way faster than any slicer iv tried yet. 
# The results of Gcode form this scrip have been amazing, absoutly the best prints ive seen yet, the rockets printed with this g code look like glass. 
# Hopfuly it will help us dicover how we can get gcode of this quality out of modles and slicers in the conventional 2d pirnting proces  
# enjoy, Rylan Grayston:


import math
file = open("RocketGenaroator.gcode", "w")

# tools for making gcode:

bounds = 20.0
mSpeed = 400.0  # speed to do moves
dSpeed = 150.0  # speed to do draws, in mm per second
step = 1  # skip N layers, use while codeing to make visulizatons faster
moveSpeed = "F" + str(mSpeed * 60) + " " 
drawSpeed = "F" + str(dSpeed * 60) + " "
drawSpeed2 = "F" + str(dSpeed * 60 * 2) + " "
drawSpeed4 = "F" + str(dSpeed * 60 * 4) + " "
laserOn = " E1.0"
laserOff = " "
layersPermm = 100.0
laserSpotDiameter = .5  #helpfull for making things overlap so they conect well



#modle spesific variables:
engineRadius = 13.2/2.0 # in mm
finRadius = 20.0 # in mm
finHeight = 30.0
totalHeight = 100.0
noseConeHeight = .55 * totalHeight
thrusterStartHeight = 6.0
finBaceLength = 6
center = 0.0
circleResolution = 100

guideLength = 18.0
guideStartHeight = thrusterStartHeight + 5.0
guideRadius = 2.4

thrusterSeed = 0.0
thrusterSeedRate = .3
thrusterSeeded = False
layers = totalHeight * layersPermm



#shapes you can just call:
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

def partialCircle(radius,resolution,posX = 0 ,posY = 0, whereDeg = 0, sizeDeg = 60):
	#this draws only part of a circle whereDeg is where it starts drawing in SizeDeg is how many deg it draws it for 
	code = ""
	deg = whereDeg
	code += "G1 " + drawSpeed +"X" +str(math.cos(math.radians(deg))* radius + posX) + " Y" + str(math.sin(math.radians(deg)) * radius + posY) + laserOff + " \n"
	#print "circle   radius: ", radius, "    resoluton: ", resolution
	for deg in range(int(whereDeg) ,int(sizeDeg+whereDeg) ,360/resolution):
		code += "G1 " + drawSpeed +"X" +str( math.cos(math.radians(deg))* radius + posX ) + " Y" + str(math.sin(math.radians(deg)) * radius + posY) + laserOn + " \n"
	return code


#the modle defined in math and loops, writen to a file as gcode

#fin
layer = 0.0
for layer in range(1,int(layers), step):
	file.write("G1 " + "Z" + str(layer/layersPermm) + " \n")
	if layer < 5:
		file.write( circle(radius = engineRadius, resolution = circleResolution ) )
	
	if layer < finHeight * layersPermm: 
		finEdge = engineRadius + finRadius - (layer/(finHeight * layersPermm)*finRadius) #this tapers the outer edge of the fin as it goes up
		if layer < thrusterStartHeight * layersPermm:
			inerFinEdge = finEdge -finBaceLength  - (finEdge- engineRadius- finBaceLength) * (layer/(thrusterStartHeight*layersPermm)) #this tapers the iner edge of the fin
		else:
			inerFinEdge = engineRadius
		
		


# seed for fin 1	
		if layer > thrusterStartHeight * layersPermm:
			thrusterSeed += thrusterSeedRate
			if thrusterSeed > 120:  # ths seeds will only gro untill each of them are 1/3 of the circle
				thrusterSeeded = True
			if not thrusterSeeded: 
				file.write( partialCircle(radius = engineRadius, resolution = circleResolution, whereDeg = -thrusterSeed/2 + 90, sizeDeg = thrusterSeed ) )
		#fin1
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(0)) * inerFinEdge ) + " Y" + str( math.cos(math.radians(0)) * inerFinEdge) + laserOff + " \n")
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(0)) * finEdge) + " Y" +       str( math.cos(math.radians(0)) * finEdge) + laserOn + " \n")
		


#seed for fin 2
		if layer > thrusterStartHeight * layersPermm and not thrusterSeeded:
			file.write( partialCircle(radius = engineRadius, resolution = circleResolution, whereDeg = -thrusterSeed/2 + 90 - 120, sizeDeg = thrusterSeed ) )
#fin 2
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(120)) * inerFinEdge ) + " Y" + str( math.cos(math.radians(120)) * inerFinEdge) + laserOff + " \n")
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(120)) * finEdge) + " Y" +       str( math.cos(math.radians(120)) * finEdge) + laserOn + " \n")

#seed for fin 3
		if layer > thrusterStartHeight * layersPermm and not thrusterSeeded:
			file.write( partialCircle(radius = engineRadius, resolution = circleResolution, whereDeg = -thrusterSeed/2 + 90 - 240, sizeDeg = thrusterSeed ) )
#fin3
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(240)) * inerFinEdge ) + " Y" + str( math.cos(math.radians(240)) * inerFinEdge) + laserOff + " \n")
		file.write("G1 " + drawSpeed +"X" +str( math.sin(math.radians(240)) * finEdge) + " Y" +       str( math.cos(math.radians(240)) * finEdge) + laserOn + " \n")



	if layer < totalHeight * layersPermm - noseConeHeight * layersPermm and layer > thrusterStartHeight * layersPermm and thrusterSeeded: # if its time to draw the straight part of the rocket toube
		file.write( circle(radius = engineRadius, resolution = circleResolution ) )
		
		
	elif layer > thrusterStartHeight * layersPermm and thrusterSeeded: # elif its time to draw the nose cone
		coneLayer = layer - (totalHeight * layersPermm - noseConeHeight * layersPermm)
		coneRadius = engineRadius - engineRadius * (coneLayer/ (noseConeHeight * layersPermm) ) * (coneLayer/ (noseConeHeight * layersPermm) ) 
		#print coneRadius		
		file.write( circle(radius = coneRadius, resolution = circleResolution ) )
	if layer > guideStartHeight * layersPermm and layer < (guideStartHeight + guideLength) * layersPermm and thrusterSeeded: #if its time to draw the rocket guide
		file.write( circle(radius = guideRadius, resolution = circleResolution, posX = engineRadius+ guideRadius - laserSpotDiameter ) )
		


 

file.close()


