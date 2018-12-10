### WIP macOS build script for Encode Sans VF, based on a build script by Mike LaGuttuta
### Run in the terminal by entering this file path
### requires a python 3 environment

############################################
################# set vars #################

glyphsSource="source/LibreCaslonText-Italic.glyphs"

## move VF into new folder of dist/ with timestamp and fontbake
timestampAndFontbakeInDist=true

## keep designspace file if you want to check values later
keepDesignspace=true

################# set vars #################
############################################

## make temp glyphs filename with "-build" suffix
tempGlyphsSource=${glyphsSource/".glyphs"/"-Build.glyphs"}

# get font name from glyphs source
italicName=`python scripts/helpers/get-italic-name.py ${glyphsSource}`

# checking that the name has been pulled out of the source file
echo "Italic Name: ${italicName}"

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

## call fontmake to make a varfont
fontmake -o ttf -g $tempGlyphsSource

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi

# ## clean up temp glyphs file
rm -rf $tempGlyphsSource

cd master_ttf

# ## fix file metadata with gftools
gftools fix-dsig --autofix ${italicName}.ttf

cd ..


# open VF in default program; hopefully you have FontView
open master_ttf/${italicName}.ttf

## if you set timestampAndFontbakeInDist variable to true, this creates a new folder in 'dist' to put it into and run fontbake on
if [ $timestampAndFontbakeInDist == true ]
then
    ## move font into folder of dist/, with timestamp, then fontbake the font
    # python3 ../scripts/distdate-and-fontbake.py ${italicName}.ttf

    newFontLocation=`python3 scripts/distdate.py master_ttf/${italicName}.ttf`

    echo "new font location is " ${newFontLocation}

    cd ${newFontLocation}

    python3 ../../scripts/fontbake.py ${italicName}.ttf

    rm -rf ../../master_ttf
else
    ttx ${italicName}.ttf
    echo "font and ttx in master_ttf folder"
fi
