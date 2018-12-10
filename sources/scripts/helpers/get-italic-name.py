import sys
from glyphsLib import GSFont

filename = sys.argv[-1]
font = GSFont(filename)

# get font name, remove spaces
italicFontName = font.familyName.replace(' ','') + '-Italic'

print(italicFontName)

sys.exit(0)