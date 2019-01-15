font = Glyphs.font

tnumWidth = 1031

tnumProblems = {}
masterIDs = []

# get layer id
for master in font.masters:
    masterIDs.append(master.id)

for glyph in font.glyphs:
    if "tnum" in glyph.name:
        for layerID in masterIDs:
            if glyph.layers[layerID].width != tnumWidth:
                tnumProblems[glyph.name] = glyph.layers[layerID].width 
    
for key in tnumProblems:
    # format for a simple markdown table
    print('| ' + str(key) + ' | ' + str(tnumProblems[key]) + ' |')
    ## if you're just using the print() panel, use this instead
    # print(str(tnumProblems[key]) + '\t' + str(key))
    # print('')

for key in tnumProblems:
    for layerID in masterIDs:
        layerGlyph = font[key].layers[layerID]
        startWidth = layerGlyph.width
        # shapeWidth = get width of glyph shape
        shapeWidth = startWidth - layerGlyph.LSB - layerGlyph.RSB

        # update layerGlyph width to make it equal correct width
        layerGlyph.width = tnumWidth

        # get new margin, and divide it into both sides to center the shape
        newMargin = tnumWidth - shapeWidth 
        layerGlyph.LSB = newMargin/2
        layerGlyph.RSB = newMargin/2

        # just to be sure that it's really correct, repeat this (margin may not exactly divide evenly)
        layerGlyph.width = tnumWidth