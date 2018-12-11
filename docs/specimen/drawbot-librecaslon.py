"""
Copy this list from font editor (in GlyphsApp, select glyphs, right click > copy > Python List)
"""

glyphNames = ["A", "Aacute", "Abreve", "Acircumflex", "Adieresis", "Agrave", "Amacron", "Aogonek", "Aring", "Aringacute", "Atilde", "AE", "AEacute", "B", "C", "Cacute", "Ccaron", "Ccedilla", "Ccircumflex", "Cdotaccent", "D", "Eth", "Dcaron", "Dcroat", "uni1E0C", "E", "Eacute", "Ebreve", "Ecaron", "Ecircumflex", "Edieresis", "Edotaccent", "uni1EB8", "Egrave", "Emacron", "Eogonek", "uni1EBC", "F", "G", "Gbreve", "Gcircumflex", "uni0122", "Gdotaccent", "H", "Hbar", "Hcircumflex", "uni1E24", "I", "IJ", "Iacute", "Ibreve", "Icircumflex", "Idieresis", "Idotaccent", "uni1ECA", "Igrave", "Imacron", "Iogonek", "Itilde", "J", "Jcircumflex", "K", "uni0136", "L", "Lacute", "Lcaron", "uni013B", "Ldot", "Lslash", "M", "N", "Nacute", "Ncaron", "uni0145", "uni1E44", "Eng", "Ntilde", "O", "Oacute", "Obreve", "Ocircumflex", "Odieresis", "uni1ECC", "Ograve", "Ohungarumlaut", "Omacron", "uni01EA", "Oslash", "Oslashacute", "Otilde", "OE", "P", "Thorn", "Q", "R", "Racute", "Rcaron", "uni0156", "uni1E5A", "S", "Sacute", "Scaron", "Scircumflex", "uni1E62", "uni018F", "T", "Tbar", "Tcaron", "uni1E6C", "U", "Uacute", "Ubreve", "Ucircumflex", "Udieresis", "uni1EE4", "Ugrave", "Uhungarumlaut", "Umacron", "Uogonek", "Uring", "Utilde", "V", "W", "Wacute", "Wcircumflex", "Wdieresis", "Wgrave", "X", "Y", "Yacute", "Ycircumflex", "Ydieresis", "Ygrave", "uni1EF8", "Z", "Zacute", "Zcaron", "Zdotaccent", "uni1E92", "uni015E", "uni0162", "uni01C4", "uni01C5", "uni01C7", "uni01C8", "uni01CA", "uni01CB", "uni01F1", "uni01F2", "uni0218", "uni021A", "a", "aacute", "abreve", "acircumflex", "adieresis", "agrave", "amacron", "aogonek", "aring", "aringacute", "atilde", "ae", "aeacute", "b", "c", "cacute", "ccaron", "ccedilla", "ccircumflex", "cdotaccent", "d", "eth", "dcaron", "dcroat", "uni1E0D", "e", "eacute", "ebreve", "ecaron", "ecircumflex", "edieresis", "edotaccent", "uni1EB9", "egrave", "emacron", "eogonek", "uni1EBD", "uni0259", "f", "g", "gbreve", "gcircumflex", "uni0123", "gdotaccent", "h", "hbar", "hcircumflex", "uni1E25", "i", "dotlessi", "iacute", "ibreve", "icircumflex", "idieresis", "uni1ECB", "igrave", "ij", "imacron", "iogonek", "itilde", "j", "uni0237", "jcircumflex", "k", "uni0137", "kgreenlandic", "l", "lacute", "lcaron", "uni013C", "ldot", "lslash", "m", "n", "nacute", "napostrophe", "ncaron", "uni0146", "uni1E45", "eng", "ntilde", "o", "oacute", "obreve", "ocircumflex", "odieresis", "uni1ECD", "ograve", "ohungarumlaut", "omacron", "uni01EB", "oslash", "oslashacute", "otilde", "oe", "p", "thorn", "q", "r", "racute", "rcaron", "uni0157", "uni1E5B", "s", "sacute", "scaron", "scircumflex", "uni1E63", "germandbls", "t", "tbar", "tcaron", "uni1E6D", "u", "uacute", "ubreve", "ucircumflex", "udieresis", "uni1EE5", "ugrave", "uhungarumlaut", "umacron", "uni015F", "uni0163", "uni01C6", "uni01C9", "uni01CC", "uni01F3", "uni0219", "uni021B", "uogonek", "uring", "utilde", "v", "w", "wacute", "wcircumflex", "wdieresis", "wgrave", "x", "y", "yacute", "ycircumflex", "ydieresis", "ygrave", "uni1EF9", "z", "zacute", "zcaron", "zdotaccent", "uni1E93", "c_t", "f_b", "f_f", "f_f_b", "f_f_h", "f_f_i", "f_f_j", "f_f_k", "f_f_l", "f_f_t", "f_h", "f_i", "f_j", "f_k", "f_l", "f_t", "s_t", "ordfeminine", "ordmasculine", "uni03BC", "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero.denominator", "one.denominator", "two.denominator", "three.denominator", "four.denominator", "five.denominator", "six.denominator", "seven.denominator", "eight.denominator", "nine.denominator", "zero.numerator", "one.numerator", "two.numerator", "three.numerator", "four.numerator", "five.numerator", "six.numerator", "seven.numerator", "eight.numerator", "nine.numerator", "zero.oldstyle", "one.oldstyle", "two.oldstyle", "three.oldstyle", "four.oldstyle", "five.oldstyle", "six.oldstyle", "seven.oldstyle", "eight.oldstyle", "nine.oldstyle", "zero.tnum", "one.tnum", "two.tnum", "three.tnum", "four.tnum", "five.tnum", "six.tnum", "seven.tnum", "eight.tnum", "nine.tnum", "uni2080", "uni2081", "uni2082", "uni2083", "uni2084", "uni2085", "uni2086", "uni2087", "uni2088", "uni2089", "uni2070", "uni00B9", "uni00B2", "uni00B3", "uni2074", "uni2075", "uni2076", "uni2077", "uni2078", "uni2079", "fraction", "onehalf", "uni2153", "uni2154", "onequarter", "threequarters", "oneeighth", "threeeighths", "fiveeighths", "seveneighths", "period", "comma", "colon", "semicolon", "ellipsis", "exclam", "exclamdown", "question", "questiondown", "periodcentered", "bullet", "asterisk", "numbersign", "slash", "backslash", "period.tnum", "comma.tnum", "colon.tnum", "semicolon.tnum", "periodcentered.tnum", "numbersign.tnum", "slash.tnum", "parenleft", "parenright", "braceleft", "braceright", "bracketleft", "bracketright", "hyphen", "uni00AD", "endash", "emdash", "underscore", "underscore.tnum", "quotesinglbase", "quotedblbase", "quotedblleft", "quotedblright", "quoteleft", "apostrophe", "quoteright", "guillemotleft", "guillemotright", "guilsinglleft", "guilsinglright", "quotedbl", "quotesingle", "quotedbl.tnum", "quotesingle.tnum", "Euro", "cent", "currency", "dollar", "florin", "sterling", "yen", "cent.tnum", "dollar.tnum", "Euro.tnum", "sterling.tnum", "yen.tnum", "plus", "minus", "multiply", "divide", "equal", "greater", "less", "plusminus", "asciitilde", "logicalnot", "asciicircum", "uni03BC.1", "percent", "perthousand", "uni2215", "uni2219", "plus.tnum", "minus.tnum", "multiply.tnum", "divide.tnum", "equal.tnum", "greater.tnum", "less.tnum", "plusminus.tnum", "percent.tnum", "at", "ampersand", "paragraph", "section", "copyright", "registered", "trademark", "degree", "bar", "brokenbar", "dagger", "daggerdbl", "uni2120", "paragraph.tnum", "section.tnum", "degree.tnum", "bar.tnum", ]


# =======================================================================

W, H = 800, 1200

newPage(W,H)

# fill(0.1)
fill(0.95,0.95,1)
# fill(0.2,0.2,0.25)
rect(0,0,W,H)

padding = 20

# =======================================================================

def drawName(yShift, colorShift):
    fontName= FormattedString()
    fontName.font("../../fonts/librecaslontext/LibreCaslonText-Italic.ttf")
    fontSizing = 270

    # fontName.fill(0,0,0,0.25)
    fontName.fill(1,0+(colorShift*0.00075),0.25)
    fontName.fontSize(fontSizing)
    fontName.tracking(0)

    fontName.lineHeight(fontSizing*.85)
    fontName.align("left")
    fontName += "Libre\n"
    fontName.align("center")
    fontName += "Caslon\n"
    fontName.align("right")
    fontName += "Text"

    textBox(fontName, (padding, -H*0.5-50, W-padding*2, (H*0.5)+padding+yShift))

nameRepeats=120

for i in range(0,nameRepeats):
    drawName(i*10,i*10)
    
    if i == nameRepeats-1:
        drawName(i*10,0)


# =======================================================================

charSet = FormattedString()

# charSet.font("./EncodeSans-VF.ttf")
charSet.font("../../fonts/librecaslontext/LibreCaslonText-Regular.ttf")
# charSet.fontVariations(wght=400.0,wdth=100.0)

# fontSizing = 30
fontSizing = 20

fontTracking = 1.8
trackingIncrease = 0.2

charSet.fontSize(fontSizing)
charSet.align("justified")
charSet.lineHeight(fontSizing*1.78)
charSet.tracking(fontTracking)
charSet.fill(0,0,0,.8)
# charSet.fill(1,1,10.75)

for index, glyph in enumerate(glyphNames):
    charSet.appendGlyph(glyph)


charSet.font("../../fonts/librecaslontext/LibreCaslonText-Medium.ttf")

fontTracking -= trackingIncrease
charSet.tracking(fontTracking)

for glyph in glyphNames:
    charSet.appendGlyph(glyph)
    
charSet.font("../../fonts/librecaslontext/LibreCaslonText-SemiBold.ttf")

fontTracking -= trackingIncrease
charSet.tracking(fontTracking)

for glyph in glyphNames:
    charSet.appendGlyph(glyph)
    
charSet.font("../../fonts/librecaslontext/LibreCaslonText-Bold.ttf")

fontTracking -= trackingIncrease
charSet.tracking(fontTracking)

for index, glyph in enumerate(glyphNames):
    charSet.appendGlyph(glyph)
    
textBox(charSet, (padding, -8, W-padding*2, H-padding/2))

# =======================================================================

saveImage("charset-light.jpg", imageResolution=144)
