from flask import Flask, render_template
import os.path, sys

app = Flask(__name__)

dic = {}

#	parser function:
# 		returns parsed dictionary

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
			depValue = []
			splitLine = line.split(": ")
			depName = splitLine[0].strip()
			for val in splitLine[1].split(" | "):
				for innerVal in val.split(", "):
					depValue.append(innerVal.split(" ")[0].strip())
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

# 	Uses demo file if user is not on system with ".../status" file.
# 	Returns parsed dictionary.

def get_packages():

	if os.path.isfile('/var/lib/dpkg/status'):
		print('\033[92m' + ":::: Path exists ::::" + '\033[0m')
		filename = "/var/lib/dpkg/status"
	else:
		print('\033[92m' + ":::: Path doesn't exist. Using demo file. ::::" + '\033[0m')
		filename = "demo.txt"

	try:
		with open(filename) as file:
			lines = file.readlines()
	except IOError as error:
		sys.exit(error)

	global dic
	dic = parser(dic, lines)

	return (dic)

@app.route("/")
def index():
	return render_template("index.html", dictionary=get_packages())

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/<package>")
def printPackage(package):
	return render_template("package.html", package=package, dictionary=get_packages())

if __name__ == "__main__":
	app.run(debug=True)