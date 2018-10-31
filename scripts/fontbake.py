import sys
import os


arg = sys.argv[-1]

if "/" in arg:
    fontFile = arg.split("/")[1]
else:
    fontFile = arg

fontName = fontFile.split(".")[0]

defaultFontPath = arg


# run fontbakery check on new font
fontbakeryCommand = f'fontbakery check-googlefonts {fontFile} --ghmarkdown fontbakery-report.md'
print("fontbakeryCommand is " + fontbakeryCommand)

print(os.system(fontbakeryCommand))