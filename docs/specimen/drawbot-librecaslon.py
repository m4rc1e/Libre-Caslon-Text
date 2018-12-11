from glyphNames import *;

W, H = 800, 1200

newPage(W,H)

# fill(0.1)
fill(0.9,0.9,0.9)
rect(0,0,W,H)

# fill(0.8)

charSet = FormattedString()

# charSet.font("./EncodeSans-VF.ttf")
charSet.font("../../fonts/librecaslontext/LibreCaslonText-Regular.ttf")
# charSet.fontVariations(wght=400.0,wdth=100.0)

# fontSizing = 30
fontSizing = 20

charSet.fontSize(fontSizing)
charSet.align("justified")
charSet.lineHeight(fontSizing*1.78)
# charSet.tracking(0.32)
charSet.tracking(3.2)
charSet.fill(.1)
# charSet += glyphSet

for glyph in glyphNames:
    charSet.appendGlyph(glyph)

charSet.font("../../fonts/librecaslontext/LibreCaslonText-Medium.ttf")

for glyph in glyphNames:
    charSet.appendGlyph(glyph)
    
charSet.font("../../fonts/librecaslontext/LibreCaslonText-SemiBold.ttf")

for glyph in glyphNames:
    charSet.appendGlyph(glyph)
    
charSet.font("../../fonts/librecaslontext/LibreCaslonText-Bold.ttf")

for glyph in glyphNames:
    charSet.appendGlyph(glyph)
    
padding = 20

stroke(1)

# rect(padding, 0, W-padding*2, H-padding)

# charSet.appendGlyph(listFontGlyphNames())
textBox(charSet, (padding, -8, W-padding*2, H-padding/2))
# print(charSet)

# saveImage("charset.pdf")


fill(1,0,0)

fontName= FormattedString()

fontSizing = 250

fontName.fill(0,0,0,0.25)
fontName.fontSize(fontSizing)
fontName.tracking(0)
fontName.align("left")
fontName.font("../../fonts/librecaslontext/LibreCaslonText-Italic.ttf")
fontName.lineHeight(fontSizing*.85)
fontName += "Libre\n"
fontName += "Caslon\n"
fontName += "Text"



textBox(fontName, (padding, 0, W-padding*2, H-padding*1.3))


saveImage("charset-tall3.png", imageResolution=144)
