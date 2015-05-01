#give this scrip a single layer made by a slicer that spells out a word and it will make a .gcode file that has many layers each layer will spell out a bit more than the last 
#speed is the number of gcodes to advance each layer. 
#This scrip would be improved if distance was the advancing factor instead of number of gcodes. for now it goes slow on curves and fast on long straight lines. 


fileToSequence = "example-layer.gcode" # nathan change this to and file you like
speed = 20

file = open(fileToSequence, "r")
codes = []
aLine = None
index = -1
while aLine != '':
	aLine = file.readline()
	codes.append(aLine)
	index += 1
	print index, " ", codes[index]

file.close()

file = open("output.gcode", "w")
totalCodesInModle = index

for layer in range(1,totalCodesInModle,speed):
	for index in range(0,layer):
		file.write(codes[index])
		
	comment = "; " +  "Rylans Layer number " + str(layer) +'\n'
	file.write(comment)	
	print comment
	file.write("G0 Z" + str(layer) + '\n')

file.close()













#distancePerFrame = 20 

#goToDistance = 0 




 
#for code in codes:
#	curentDistance += getDistance()
#	if currentDistance > goToDistance:
#		break








