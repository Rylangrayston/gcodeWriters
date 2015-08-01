# test print with surface flow relive holes 


#once upon a time rylan at peachy wanted to see if adding little holes 
# to a print would alow the resin to flow into the center of the print 
# at chosen points, as the theory goes, perhaps once a hole has done #the job of leting resin in, that #hole can be sealed up with a long #exposure, while at the same time another hole somewere else can be #opening up to continue the flow of resin into the print. 

# the number of layers we draw per mm of z height rise will be defined as
layersPermm = 100.0

# the total height of the test print will be defined as 
totalHeight =40.0 # in mm

#the rate of flow alowed by a hole should grow proportionaly with the aria that is being printed that #layer. this could be rather complicated as there are fluid dynamics to be considerd, looking into the 
# a flow calcuator for non presurized pipes could be valuble,  hydrolic radius/ weted parimiter and #time to alow for flow between layers could be calculated from the aria that must be filled with resin #for that layer. 
# this is a first go and I will not be caluclating any of this for now, instead ill just write the hole #size to be a percentage of the wall size its in. It is expected that this hole will can not grow fast #enugh to fill larger arias with resin and at some size, filling an empty ocean would take days evan if #water came from all sides :) 

maxWidth = 40.0  # the largest the print will get in the x and y 
holeFactor = 0.33 # what percentage of one wall will be a hole
HoleLength = maxWidth * holeFactor 

holeHeight = 3 # the talest a hole will get before being healed 
holeOverlapHeight = 1 # what distance in the z will the holes overlap

holeHeight -= holeOverlapHeight
layersPerHole = holeHeight * layersPermm

healExposureFactor = 2.5 #  how many more photons the aria over a hole will get when being healed




import math
file = open("surfaceFlowRelifeHole.gcode", "w")


mSpeed = 400.0  # speed to do moves
dSpeed = 100.0  # speed to do draws, in mm per second
step = 1  # skip N layers, use while codeing to make visulizatons faster
moveSpeed = "F" + str(mSpeed * 60) + " " 
drawSpeed = "F" + str(dSpeed * 60) + " "
healSpeed = "F" + str( (dSpeed * 60)/ healExposureFactor ) + " "

laserOn = " E1.0"
laserOff = " "
laserSpotDiameter = .5  #helpfull for making things overlap so they conect well
layers = totalHeight * layersPermm
code = ""

currentLayer = 0

scaleFactor = 1.0

scaleCount = 0

# G1 F9000.0 X6.59095492938 Y0.345417311203 E1.0 

def leftHoleLayer(scale):

	scaledWidth = maxWidth * scale 
	scaledHoleLength = HoleLength *scale

	code = ""

	code += "G1 " + "Z" + str(currentLayer/layersPermm) + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledWidth/2 ) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOff + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + healSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledWidth/2) + laserOn + " \n"
	return(code)
	
def rightHoleLayer(scale):

	scaledWidth = maxWidth * scale 
	scaledHoleLength = HoleLength *scale

	code = ""

	code += "G1 " + "Z" + str(currentLayer/layersPermm) + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledWidth/2 ) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + healSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOff + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledWidth/2) + laserOn + " \n"
	return(code)
	

def twoHolesLayer(scale):

	scaledWidth = maxWidth * scale 
	scaledHoleLength = HoleLength *scale

	code = ""

	code += "G1 " + "Z" + str(currentLayer/layersPermm) + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledWidth/2 ) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOff + " \n"

	code += "G1 " + drawSpeed + "X" + str(scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledWidth/2) + laserOn + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(scaledHoleLength/2) + laserOn + " \n"
 	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledHoleLength/2) + laserOff + " \n"

	code += "G1 " + drawSpeed + "X" + str(-scaledWidth/2) + " Y" + str(-scaledWidth/2) + laserOn + " \n"
	return(code)
	

def leftHole(scaleChange):
	global currentLayer
	global scaleCount

	for holeyLayer in range(1,int(layersPerHole),1):
		currentLayer += 1
		scaleCount += scaleChange
		scaleFactor = scaleCount / layers
		file.write( leftHoleLayer(scale = scaleFactor) )
		print(currentLayer)



def rightHole(scaleChange):
	global currentLayer
	global scaleCount

	for holeyLayer in range(1,int(layersPerHole),1):
		currentLayer += 1
		scaleCount += scaleChange
		scaleFactor = scaleCount / layers
		file.write( rightHoleLayer(scale = scaleFactor) )
		print(currentLayer)


def twoHoles(scaleChange):
	global currentLayer
	global scaleCount

	for holeyLayer in range(1,int(layersPerHole),1):
		currentLayer += 1
		scaleCount += scaleChange
		scaleFactor = scaleCount / layers
		file.write( twoHolesLayer(scale = scaleFactor) )
		print(currentLayer)





while currentLayer < layers * .5 :

	leftHole( scaleChange = 1 )
	twoHoles( scaleChange = 1 )
	rightHole( scaleChange = 1 )
	twoHoles( scaleChange = 1 )


while currentLayer < layers * 1 :


	leftHole( scaleChange = -1 ) 
	twoHoles( scaleChange = -1)
	rightHole( scaleChange = -1 )
	twoHoles( scaleChange = -1 )






file.close()


































