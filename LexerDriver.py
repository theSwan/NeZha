import Lexer
from Symbols import EOF


def writeln(*args):
	for arg in args:
		f.write(str(arg))
	f.write("\n")


def main(sourceText):
	global f
	f = open(outputFilename, "w")
	writeln("Here are the tokens returned by the lexer:")

	Lexer.initialize(sourceText)

	while True:
		token = Lexer.get()
		writeln(token.show(True))
		if token.type == EOF:
			break
	f.close()


if __name__ == "__main__":
	outputFilename = "output/test_output.txt"
	sourceFilename = "input/test.nz"
	sourceText = open(sourceFilename).read()
	main(sourceText)
	print(open(outputFilename).read())
