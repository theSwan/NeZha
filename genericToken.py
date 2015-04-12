class LexerError(Exception):
	pass


class Token:
	"""
	A Token object is the kind of thing that the Lexer returns.
	It holds:
	- the text of the token (self.cargo)
	- the type of token that it is
	- the line number and column index where the token starts
	"""

	def __init__(self, startChar):
		self.cargo = startChar.cargo

		self.sourceText = startChar.sourceText
		self.lineIndex = startChar.lineIndex
		self.colIndex = startChar.colIndex

		self.type = None

	#-------------------------------------------------------------------
	#  return a displayable string representation of the token
	#-------------------------------------------------------------------
	def show(self, showLineNumbers = False, **kwargs):
		"""
		align=True shows token type left justified with dot leaders.
		Specify align=False to turn this feature OFF.		
		"""
		align = kwargs.get("align", True)
		if align: 
			tokenTypeLen = 12
			space = " "
		else: 
			tokenTypeLen = 0
			space = ""
			
		if showLineNumbers:
			s = str(self.lineIndex).rjust(6) + str(self.colIndex).rjust(4) + "  "
		else:
			s = ""
			
		if self.type == self.cargo: 
			s = s + "Symbol".ljust(tokenTypeLen, ".") + ":" + space + self.type
		elif self.type == "Whitespace": 
			s = s + "Whitespace".ljust(tokenTypeLen, ".") + ":" + space + repr(self.cargo)
		else:
			s = s + self.type.ljust(tokenTypeLen, ".") + ":" + space + self.cargo
		return s
			
	guts = property(show)

	def abort(self, msg):
		raise LexerError("\nline " + str(self.lineIndex + 1) + " near column " + str(self.colIndex + 1) + ":" + msg)
