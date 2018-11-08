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
VFname=`python scripts/helpers/get-font-name.py ${glyphsSource}`
# checking that the name has been pulled out of the source file
echo "VF Name: ${VFname}"

## copy Glyphs file into temp file
cp $glyphsSource $tempGlyphsSource

## call fontmake to make a varfont
fontmake -o variable -g $tempGlyphsSource

if [ $keepDesignspace == true ]
then
    echo "designspace in master_ufo folder"
else
    rm -rf master_ufo
fi

## clean up temp glyphs file
rm -rf $tempGlyphsSource

cd variable_ttf

## fix file metadata with gftools
gftools fix-dsig --autofix ${VFname}.ttf


rm -rf ${VFname}-backup-fonttools-prep-gasp.ttf

cd ..

# cd variable_ttf
# open VF in default program; hopefully you have FontView
open variable_ttf/${VFname}.ttf

## if you set timestampAndFontbakeInDist variable to true, this creates a new folder in 'dist' to put it into and run fontbake on
if [ $timestampAndFontbakeInDist == true ]
then
    ## move font into folder of dist/, with timestamp, then fontbake the font
    # python3 ../scripts/distdate-and-fontbake.py ${VFname}.ttf

    newFontLocation=`python3 scripts/distdate.py variable_ttf/${VFname}.ttf`

    echo "new VF location is " ${newFontLocation}

    cd ${newFontLocation}

    python3 ../../scripts/fontbake.py ${VFname}.ttf

    rm -rf ../../variable_ttf
else
    ttx ${VFname}.ttf
    echo "font and ttx in variable_ttf folder"
fi
