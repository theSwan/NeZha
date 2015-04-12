Keywords = """
if
then
else
elif
end
while
print
return
def
in
"""
Keywords = Keywords.split()

OneCharacterSymbols = """
=
( )
[ ]
< > #
/ * + -
! & | ^
. ; : ,
"""
OneCharacterSymbols = OneCharacterSymbols.split()

TwoCharacterSymbols = """
==
<=
>=
!=
**
"""

TwoCharacterSymbols = TwoCharacterSymbols.split()

ThreeCharacterSymbols = """
<<<
>>>
<->
"""

ThreeCharacterSymbols = ThreeCharacterSymbols.split()

import string

IDENTIFIER_STARTCHARS = string.letters
IDENTIFIER_CHARS      = string.letters + string.digits + "_"

NUMBER_STARTCHARS     = string.digits
NUMBER_CHARS          = string.digits + "."

STRING_STARTCHARS = "'" + '"'
LINE_MARK = "\n"
WHITESPACE_CHARS  = " \t\n"


STRING             = "String"
IDENTIFIER         = "Identifier"

NUMBER             = "Number"
WHITESPACE         = "Whitespace"
COMMENT            = "Comment"
EOF                = "Eof"
