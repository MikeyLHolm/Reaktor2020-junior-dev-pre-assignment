#!/usr/bin/python3
import os.path, sys

#	parser function:
# 		returns parsed dictionary
#	issues:
#		parsing version numbers or "|" is incomplete

def parser(dic, lines):

	for line in lines:
		if len(line.strip()) == 0:
			continue
		if not line.startswith(("Package", "Depends", "Description", " ")):
			continue
		if line.startswith(" /"):
			continue
		if line.startswith('Package'):
			nameLine = line.strip()
			name = nameLine.split(": ")[1]
			dic[name] = {}

		if line.startswith('Depends'):
			splitLine = line.split(":")
			depName = splitLine[0].strip()
			depValue = splitLine[1].strip().split(", ")
			dic[name][depName] = depValue

		if line.startswith('Description'):
			splitLine = line.split(":")
			descName = splitLine[0].strip()
			descValue = splitLine[1].strip()
			dic[name][descName] = descValue

		if line.startswith(' '):
			descValue += line.rstrip()
			dic[name][descName] = descValue

	return dic

def main():

	if os.path.isfile('\033[92m' + '/var/lib/dpkg/status' + '\033[0m'):
		print(":::: Path exists ::::")
		filename = "/var/lib/dpkg/status"
	else:
		print('\033[92m' + ":::: Path doesn't exist. Using demo file. ::::" + '\033[0m')
		#filename = "status"
		filename = "text.txt"

	try:
		with open(filename) as file:
			lines = file.readlines()
	except IOError as error:
		sys.exit(error)

	dic = {}
	dic = parser(dic, lines)

	print (dic)

if __name__ == "__main__":
    main()