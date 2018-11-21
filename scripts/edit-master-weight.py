__doc__= """
    Work in progress.

    Attempts to add new master at interpolated position, then delete existing master.
"""


import sys
import os
from Glyphs import *

def main():

    oldMasterWeightValue = float(sys.argv[-2])
    newMasterWeightValue = float(sys.argv[-1])

    filename = sys.argv[-3]
    directory = os.getcwd()
    document = Glyphs.open((str(directory + "/" + filename)), False)

    font = document.font()

    # create new instance
    newInstance = Glyphs.objectWithClassName_("GSInstance")



    # set new instance weight value to variable from above
    # newInstance.weightValue = newMasterWeightValue
    newInstance.setInterpolationWeight_(newMasterWeightValue)
    font.instances().append(newInstance)

    print(newInstance)
    print(font.instances()[-1])

    for instance in font.instances():
        print(instance, instance.interpolationWeight())

    # make an interpolated font of the new instance
    instanceFont = font.instances()[0].interpolatedFont()

    print(instanceFont)
    # I expect this to only print 1 master, but it prints the main font's 2 masters
    print(instanceFont.fontMasters())

    # add the master of the interpolated font to the masters
    font.fontMasters().append(instanceFont.fontMasters()[0])
    # get the id from the master of the interpolated font
    newMasterID = instanceFont.fontMasters()[0].id


    # for i, master in enumerate(font.fontMasters()):
    #     print(master)

    # for glyph in font.glyphs():
    #     print(glyph.name())

    for glyph in font.glyphs():
        # make variable for glyph of interpolated font
        instanceGlyph = instanceFont.glyphs()[glyph.name()]
        # bring glyph data into glyph of new master
        glyph.layers[newMasterID] = instanceGlyph.layers[newMasterID]

    # bring kerning in from interpolated font
    font.kerning[newMasterID] = instanceFont.kerning[newMasterID]

    for i, instance in enumerate(font.instances()):
        # delete generated instance
        if instance.weightValue == newMasterWeightValue:
            print("delete " + str(instance))
            del font.instances()[i]

    for i, master in enumerate(font.fontMasters()):
        # delete old master
        if master.weightValue == oldMasterWeightValue:
            print("delete " + str(master))
            del font.fontMasters()[i]
        # set new master value as old master value (round to nearest integer to match)
        if round(master.weightValue) == round(newMasterWeightValue):
            print("update weight value of " + str(master))
            font.fontMasters()[i].weightValue = oldMasterWeightValue

    font.close(False)

if __name__ == '__main__':
    main()