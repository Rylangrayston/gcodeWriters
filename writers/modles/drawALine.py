#hellow world of gcode for a peachy printer


file = open("drawALine.gcode", "w")

# a gcode looks like this:
# G1 F2000.0 X10.0 Y10.0 E1.0 

code = "G1 " + "F2000.0 " + "X" + str(10.0) + " Y" + str(10.0) + " E1.0" + " \n"
print(code)
file.write(code)

file.close()

