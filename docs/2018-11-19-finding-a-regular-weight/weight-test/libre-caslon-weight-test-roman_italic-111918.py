# RENDER WITH: http://www.drawbot.com/
# assumes you are running via a Drawbot module from the command line, while in this script's directory

from drawBot import *
# import os

# sample = """\
# nnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnnnlalnnlblnnlclnnldlnnlelnnlflnnlglnnlhlnnlilnnljlnnlklnnlllnnlmlnnlnlnnlolnnlplnnlqlnnlrlnnlslnnltlnnlulnnlvlnnlwlnnlxlnnlylnnlzlnnl
# """
shortSample = "anbncndnenfngnhninjnknlnmnnnonpnqnrnsntnunvnwnxnynzanbncndnenfngnhninjnknlnmnnnonpnqnrnsntnunvnwnxnynz"

# size('Letter')
# W, H = width(), height()

# W, H= 800,800
W, H= 1000,1000
# size(W,H)

print(W, H)


# fontSize = 16
fontSize = 32

# caslonWeight = 450

def placeText(fontName,topMargin, weight=0):
    if weight > 1:
        fontVariations(wght=weight)
    font(fontName,fontSize)
    textBoxSize = (margin, H-topMargin, W-margin*2, boxHeight)
    textBox(shortSample, textBoxSize)


lines = int(floor(H / fontSize / 2.15))

print(lines)

# for num in range(20):
for num in range(4):    
    newPage(W,H)
    frameDuration(.25)
    caslonWeight = 400 + num*5
    
    print(caslonWeight)
    fill(.95,.95,.95)
    rect(0,0,W, H)
    
    im = ImageObject()
    
    with im:
        for i in range(lines):
            
            fontSize = 32
            margin= fontSize
            boxHeight= fontSize
            lineHeight(fontSize*1)
            lineHeight(fontSize*1)
            # fontVariations(wght=450)
            fill(0)
            # rect(0,boxHeight*i*2,boxHeight,boxHeight)
            topMargin = margin * i*2 + margin*2
            placeText("./LibreCaslonText-VF.ttf",topMargin,weight=caslonWeight)
            placeText("./LibreCaslonText-Italic.ttf",topMargin+boxHeight)

    # apply some filters if desired
    # im.gaussianBlur(0.1)

    # get the offset (with a blur this will be negative)
    x, y = im.offset()
    
    image(im, (0+x, 0+y))
    
    fontSize = 16
    margin= fontSize
    boxHeight= fontSize
    lineHeight(fontSize*1)

    
    fill(0)
    font("IBM Plex Mono", 16)
    lineHeight(fontSize*1)
    textBox("wght: " + str(caslonWeight), (10,10,100,16))




# imgPath = "../assets/weight-test-roman_italic-noblur-big-111918.mp4" # do 50 frames with a wght increase rate of 2 
imgPath = "../assets/weight-test-roman_italic-noblur-big-111918.gif" # do 20 frames with a wght increase rate of 5
# saveImage(imgPath)
# saveImage(imgPath, imageResolution=300)
# os.system('open %s' % imgPath)