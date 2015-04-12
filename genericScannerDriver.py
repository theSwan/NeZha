import genericScanner as Scanner


def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")


def main(sourceText):
	global f
	f = open(outputFilename, "w")

	writeln("Here are the characters returned by the scanner:")
	writeln("  line col  character")

	Scanner.initialize(sourceText)

	character = Scanner.get()
	while True:
		writeln(character)
		if character.cargo == Scanner.ENDMARK:
			break
		character = Scanner.get()

	f.close()


if __name__ == "__main__":
	outputFilename = "output\\genericScannerDriver_output.txt"
	sourceText = open("input\\nxx1.txt").read()
	main(sourceText)
	print open(outputFilename).read()
