ENDMARK = "\0"


class Character:
	"""
	A Character object holds
		- one character (self.cargo)
		- the index of the character's position in the sourceText.
		- the index of the line where the character was found in the sourceText.
		- the index of the column in the line where the character was found in the sourceText.
		- (a reference to) the entire sourceText (self.sourceText)
	"""

	def __init__(self, c, lineIndex, colIndex, sourceIndex, sourceText):
		self.cargo = c
		self.sourceIndex = sourceIndex
		self.lineIndex = lineIndex
		self.colIndex = colIndex
		self.sourceText = sourceText

	def __str__(self):
		"""
		In Python, the __str__ method returns a string representation
		of an object.
		"""
		cargo = self.cargo
		if cargo == " ":
			cargo = "   space"
		elif cargo == "\n":
			cargo = "   newline"
		elif cargo == "\t":
			cargo = "   tab"
		elif cargo == ENDMARK:
			cargo = "   eof"

		return str(self.lineIndex).rjust(6) + str(self.colIndex).rjust(4) + "  " + cargo

