#!/usr/bin/python3


def main():

	filename = "text.txt"
	dict = {}
	with open(filename, "r") as f:
		for line in f:
			items = line.split()
			key, values = items[0], items[1:]
			dict[key] = values

	print(dict)
	# contents = f.read()
	# print(contents)

if __name__ == "__main__":
    main()