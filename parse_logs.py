import re

def __main__(output_file):
	file = raw_input("Enter the path to the logs file :  ")
	try:
		file = open(file, 'r')
	except:
		print("Can't Open this file \n")

	for i in file.readlines():
		line = i.split( )
		log = "Ip : " + line[0] + "  Method : " + line[5] + "  URI : " + line[6]+ "  User Agent : " + line[11] + "\n"
		if output_file:
			output_file.write(log)
		else:
		    print(log)


