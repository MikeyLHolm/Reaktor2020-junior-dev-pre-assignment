#!/usr/bin/python3
import re

def parseDepends(str, depends):
	# parse depends to a list.
	print ("deps: " + str)
	q = str.split(", ")
	# print(type(q))
	for zet in q:
		z = zet.split(" ")
	print (z)
	depends.append(z)
	print (depends)
	return (depends)

def main():

	filename = "status"
	#filename = "text.txt"

	#filu = open(filename, "r")

	file = open(filename, "r")
	lines = file.readlines()
	file.close

	dic = {}
	depends = []

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
			depValue = splitLine[1].strip()
			dic[name][depName] = depValue
			depends = parseDepends(dic[name][depName], depends)

		if line.startswith('Description'):
			splitLine = line.split(":")
			descName = splitLine[0].strip()
			descValue = splitLine[1].strip()
			dic[name][descName] = descValue

		if line.startswith(' '):
			descValue += line.rstrip()
			dic[name][descName] = descValue

		#print (d)
		#parseDepends(d[name][depName])

	#print (d)

	# with open(filename, "r") as f:
	# 	for line in f:
	# 		items = line.split(':')
	# 		print(items[0])

	# 		print(items[1:])
	# 		key, values = items[0], items[1:]
	# 		if key in {"Package", "Depends", "Description"}:
	# 			d[key] = values

	# print(json.dumps(d, indent=4))
	# for k in d:
	# 	print(k)
	# 	for v in d[k]:
	# 		print(v)

if __name__ == "__main__":
    main()