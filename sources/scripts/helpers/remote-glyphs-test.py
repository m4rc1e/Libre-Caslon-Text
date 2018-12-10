import sys
import os
from Glyphs import *

def main():

    filename = sys.argv[-1]
    directory = os.getcwd()
    document = Glyphs.open((str(directory + "/" + filename)), False)

    font = document.font()

    print(font) # GSFont <0x7f865b814b70>: Libre Caslon Text (537)

    # Goal: access objects in font, such as masters and instances, plus their methods, such as instance.interpolatedFont

    for instance in font.instances():
        print(instance)
        print(instance.interpolatedFont)
    # for glyph in font.glyphs():
    #     print(glyph)

    for i, master in enumerate(font.fontMasters()):
        print(i, master)

    # doesn't work :/
    # AttributeError: 'NSDistantObject' object has no attribute 'masters'
    # for master in font.masters():
    #     print(master)

    font.close(False)

if __name__ == '__main__':
    main()