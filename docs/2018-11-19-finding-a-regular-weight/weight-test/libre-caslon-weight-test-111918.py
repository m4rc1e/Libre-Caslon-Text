# RENDER WITH: http://www.drawbot.com/
# assumes you are running via a Drawbot module from the command line, while in this script's directory

from drawBot import *
import math
import os

# weight test for Libre Caslon Text Regular vs comparable typefaces

# sample = """\
# One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a little too small, lay peacefully between its four familiar walls. A collection of textile samples lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer.
# """
sample = """\
nnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnn
"""
# sample = """\
# nnnoooiiillliiiooonnn
# """


# size('Letter')
size(612, 612)
W, H = width(), height()

print(W, H)

margin= 50
boxHeight= 100


# background
fill(.95,.95,.95)
rect(0,0,W, H)

fontSize = 12
lineHeight(fontSize*1)
fill(0)

caslonWeight = 450


def placeText(fontName, index, weight=0):
    if weight > 0:
        fontVariations(wght=weight)
    font(fontName,fontSize)
    topMargin = (boxHeight * (index +1) + margin + (10 * index))
    textBoxSize = (margin, H-topMargin, W-margin*2, boxHeight)
    textBox(sample, textBoxSize)

    # with savedState():
    #     fill(0,0,0,0)
    #     stroke(1,0,0)
    #     rect(textBoxSize[0],textBoxSize[1],textBoxSize[2],textBoxSize[3])

    # add captions of font names
    with savedState():
        fill(0.2,0.2,1)
        rotate(90)
        captionWidth = boxHeight
        font("IBM Plex Sans",7)
        textBoxSize = (H-topMargin-fontSize/4, 0-margin*1.4, captionWidth, 40)
        if weight > 0:
            textBox(fontName + " (" + str(weight) + ")", textBoxSize, align="right")
        else:
            textBox(fontName, textBoxSize, align="right")
        fill(1,0,0)
        rect(0,0,100,100)

# placeText("Times New Roman", 0)
placeText("Times New Roman", 0)
placeText("Times", 1)

# fontVariations(wght=450)
placeText("LibreCaslonText-VF.ttf", 2,weight=caslonWeight)
placeText("LibreCaslonText-Italic.ttf", 3)
placeText("Georgia", 4)

# imgPath = "../assets/weight-test-book_text-111918.png"
imgPath = "../assets/weight-test-spacing_string-"+ str(caslonWeight) +"og-111918.png"
# saveImage(imgPath)
saveImage(imgPath, imageResolution=300)
# os.system('open %s' % imgPath)