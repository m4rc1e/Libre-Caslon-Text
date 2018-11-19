# RENDER WITH: http://www.drawbot.com/
from drawBot import *
import math
import os
import subprocess

# weight test for Libre Caslon Text Regular vs comparable typefaces

sample = """\
One morning, when Gregor Samsa woke from troubled dreams, he found himself transformed in his bed into a horrible vermin. He lay on his armour-like back, and if he lifted his head a little he could see his brown belly, slightly domed and divided by arches into stiff sections. The bedding was hardly able to cover it and seemed ready to slide off any moment. His many legs, pitifully thin compared with the size of the rest of him, waved about helplessly as he looked. "What's happened to me?" he thought. It wasn't a dream. His room, a proper human room although a little too small, lay peacefully between its four familiar walls. A collection of textile samples lay spread out on the table - Samsa was a travelling salesman - and above it there hung a picture that he had recently cut out of an illustrated magazine and housed in a nice, gilded frame. It showed a lady fitted out with a fur hat and fur boa who sat upright, raising a heavy fur muff that covered the whole of her lower arm towards the viewer.
"""

size('Letter')
W, H = width(), height()

margin= 50
boxHeight= 100


# background
fill(1,.95,.95)
rect(0,0,W, H)

fontSize = 14
lineHeight(fontSize*1)
fill(0)

def placeText(fontName, index):
    font(fontName,fontSize)
    topMargin = (boxHeight * (index +1) + margin + (10 * index))
    textBoxSize = (margin, H-topMargin, W-margin*2, boxHeight)
    textBox(sample, textBoxSize)

placeText("Times New Roman", 0)
placeText("Times", 1)
placeText("Tinos", 2)
placeText("docs/2018-11-19-finding-a-regular-weight/weight-test/LibreCaslonText-VF.ttf", 3)


imgPath = "docs/2018-11-19-finding-a-regular-weight/assets/weight-test-111918.png"
# saveImage(imgPath)
saveImage(imgPath, imageResolution=144)
# os.system('open %s' % imgPath)

# command = "pqiv --watch-files=on --hide-info-box" + imgPath
# subprocess.call(command, shell=True)