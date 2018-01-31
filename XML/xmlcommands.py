#!/usr/bin/python

#uses xmltodict library
import xmltodict

if ( __name__ == "__main__"):
	AppVersion = "1.0"

	with open('commands.xml') as fd:
		doc = xmltodict.parse(fd.read())
		
	if (doc['commandlist']['@appversion'] != AppVersion):
		print("Error, wrong appversion")
		quit()
		
	print("Version matches")
	
	Commands = doc['commandlist']
	while 1:
		str = input('command> ')
		if (str == 'q'):
			quit()
		calledCommand = Commands[str]
		print("#####",calledCommand['@name'],"#####")
		print(calledCommand['desc'])
		print(calledCommand['data'])