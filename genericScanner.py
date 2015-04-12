from genericCharacter import *

"""
A Scanner object reads through the sourceText
and returns one character at a time.
"""


def initialize(sourceTextArg):
	global sourceText, lastIndex, sourceIndex, lineIndex, colIndex
	sourceText = sourceTextArg
	lastIndex = len(sourceText) - 1
	sourceIndex = -1
	lineIndex = 0
	colIndex = -1


def get():
	"""
	Return the next character in sourceText.
	"""
	global lastIndex, sourceIndex, lineIndex, colIndex

	sourceIndex += 1

	if sourceIndex > 0:
		if sourceText[sourceIndex - 1] == "\n":
			lineIndex += 1
			colIndex = -1

	colIndex += 1

	if sourceIndex > lastIndex:
		char = Character(ENDMARK, lineIndex, colIndex, sourceIndex, sourceText)
	else:
		c = sourceText[sourceIndex]
		char = Character(c, lineIndex, colIndex, sourceIndex, sourceText)

	return char


def lookahead(offset = 1):
	"""
	Return a string (not a Character object) containing the character
	at position:
			sourceIndex + offset
	Note that we do NOT move our current position in the sourceText.
	That is,  we do NOT change the value of sourceIndex.
	"""
	index = sourceIndex + offset

	if index > lastIndex:
		return ENDMARK
	else:
		return sourceText[index]